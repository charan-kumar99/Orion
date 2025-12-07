"""Flask Web Application for Orion Voice Assistant"""
from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import speech_recognition as sr
from gtts import gTTS
import os
import threading
import time
from datetime import datetime
from dotenv import load_dotenv
import config
from client import get_ai_response
import wikipedia
import musiclibrary
import re
import io
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
google_api_key = os.getenv('GOOGLE_API_KEY')
if google_api_key:
    genai.configure(api_key=google_api_key)

def get_gemini_response(query):
    """Get AI response from Google Gemini"""
    try:
        if not google_api_key:
            print("Gemini API: No API key configured")
            return None
        
        print(f"Gemini API: Sending query: {query[:50]}...")
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(query)
        print(f"Gemini API: Response received successfully")
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

app = Flask(__name__)
CORS(app)

# Global state
assistant_state = {
    'listening': False,
    'last_command': '',
    'last_response': '',
    'history': []
}

class VoiceAssistant:
    """Voice assistant handler for web interface"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def process_command(self, command):
        """Process command and return response"""
        command = command.lower()
        response = ""
        
        # Exit command
        if "exit" in command or "quit" in command:
            response = "Goodbye! Refresh to restart."
        
        # Time and date
        elif "time" in command:
            now = datetime.now()
            time_str = now.strftime("%I:%M %p")
            response = f"The time is {time_str}"
        
        elif "date" in command or "today" in command:
            now = datetime.now()
            date_str = now.strftime("%B %d, %Y")
            response = f"Today is {date_str}"
        
        # Calculations
        elif "calculate" in command or ("what" in command and any(op in command for op in ["plus", "minus", "times", "divided"])):
            try:
                expression = re.sub(r'(calculate|what is|whats)', '', command, flags=re.IGNORECASE).strip()
                expression = expression.replace('plus', '+').replace('minus', '-')
                expression = expression.replace('times', '*').replace('multiplied by', '*')
                expression = expression.replace('divided by', '/').replace('divide', '/')
                
                # Validate expression contains only safe characters
                if re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
                    result = eval(expression, {"__builtins__": None}, {})
                    response = f"The answer is {result}"
                else:
                    response = "Sorry, I can only calculate mathematical expressions."
            except ZeroDivisionError:
                response = "Cannot divide by zero."
            except Exception as e:
                response = "Sorry, I couldn't perform that calculation. Please try again."
        
        # Show songs
        elif "show songs" in command or "list songs" in command:
            songs = musiclibrary.get_all_song_names()
            response = f"Available songs ({len(songs)}): " + ", ".join(songs[:10])
            if len(songs) > 10:
                response += f" and {len(songs) - 10} more..."
        
        # Web browsing
        elif "open google" in command:
            response = "Opening Google..."
        elif "open youtube" in command:
            response = "Opening YouTube..."
        elif "open facebook" in command:
            response = "Opening Facebook..."
        elif "open linkedin" in command:
            response = "Opening LinkedIn..."
        
        # Music playback
        elif command.startswith("play"):
            song_name = command.replace("play", "").strip().lower().replace(" ", "_")
            if song_name in musiclibrary.music:
                url = musiclibrary.music[song_name]
                response = f"Playing {song_name.replace('_', ' ')}. Opening in new tab..."
            else:
                response = f"Sorry, I don't have '{song_name.replace('_', ' ')}' in my library. Try 'show songs' to see available music."
        
        # AI or Wikipedia
        else:
            # Try Google Gemini AI response first
            if google_api_key:
                ai_response = get_gemini_response(command)
                if ai_response:
                    response = ai_response
                else:
                    response = self._search_wikipedia(command)
            else:
                # Fallback to Wikipedia if no API key
                response = self._search_wikipedia(command)
        
        return response
    
    def _search_wikipedia(self, query):
        """Search Wikipedia and return result"""
        try:
            summary = wikipedia.summary(query, sentences=2)
            return summary
        except wikipedia.exceptions.DisambiguationError:
            return f"Multiple results found for '{query}'. Please be more specific."
        except wikipedia.exceptions.PageError:
            return f"Sorry, I couldn't find information about '{query}'."
        except:
            return "Sorry, I encountered an error searching Wikipedia."
    
    def text_to_speech(self, text):
        """Convert text to speech audio"""
        try:
            tts = gTTS(text, lang=config.TTS_LANGUAGE)
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            return audio_fp
        except Exception as e:
            print(f"TTS Error: {e}")
            return None

# Initialize assistant
assistant = VoiceAssistant()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html', assistant_name=config.ASSISTANT_NAME)

@app.route('/api/status')
def status():
    """Get assistant status"""
    return jsonify({
        'status': 'online',
        'name': config.ASSISTANT_NAME,
        'gemini_enabled': bool(google_api_key),
        'song_count': musiclibrary.get_song_count()
    })

@app.route('/api/process', methods=['POST'])
def process():
    """Process a command from the web interface"""
    data = request.json
    command = data.get('command', '')
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    # Process the command
    response = assistant.process_command(command)
    
    # Update state
    assistant_state['last_command'] = command
    assistant_state['last_response'] = response
    assistant_state['history'].append({
        'command': command,
        'response': response,
        'timestamp': datetime.now().isoformat()
    })
    
    # Keep only last 50 items
    if len(assistant_state['history']) > 50:
        assistant_state['history'] = assistant_state['history'][-50:]
    
    return jsonify({
        'command': command,
        'response': response,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/tts', methods=['POST'])
def text_to_speech_endpoint():
    """Convert text to speech audio"""
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    audio_fp = assistant.text_to_speech(text)
    
    if audio_fp:
        return Response(audio_fp.read(), mimetype='audio/mpeg')
    else:
        return jsonify({'error': 'TTS failed'}), 500

@app.route('/api/songs')
def get_songs():
    """Get list of available songs"""
    songs = []
    for key, url in musiclibrary.music.items():
        songs.append({
            'name': key.replace('_', ' ').title(),
            'key': key,
            'url': url
        })
    return jsonify({'songs': songs})

@app.route('/api/history')
def get_history():
    """Get command history"""
    return jsonify({'history': assistant_state['history']})

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """Clear command history"""
    assistant_state['history'] = []
    return jsonify({'success': True})

if __name__ == '__main__':
    print("="*50)
    print(f"🚀 {config.ASSISTANT_NAME} Web Interface Starting...")
    print("="*50)
    print(f"🌐 Open your browser to: http://localhost:5000")
    print(f"🤖 Google Gemini AI: {'Enabled ✅' if google_api_key else 'Disabled ❌'}")
    print(f"🎵 Songs available: {musiclibrary.get_song_count()}")
    print("="*50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
