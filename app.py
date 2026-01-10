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
        action = None
        url = None
        
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
            response = "I can play any song you'd like! Just say 'play' followed by the song name. For example: 'play Blinding Lights' or 'play Tum Hi Ho'."
        
        # Web browsing
        elif "open google" in command:
            action = "pending_action"
            url = "https://google.com"
            response = "Ready to open Google"
        elif "open youtube" in command:
            action = "pending_action"
            url = "https://youtube.com"
            response = "Ready to open YouTube"
        elif "open facebook" in command:
            action = "pending_action"
            url = "https://facebook.com"
            response = "Ready to open Facebook"
        elif "open linkedin" in command:
            action = "pending_action"
            url = "https://linkedin.com"
            response = "Ready to open LinkedIn"
        
        # Music playback
        elif command.startswith("play"):
            song_name = command.replace("play", "").strip()
            
            if not song_name:
                response = "What would you like me to play?"
            else:
                # First, check if song exists in the music library
                song_key = song_name.lower().replace(" ", "_")
                
                # Search for exact or partial match in music library
                found_url = None
                found_song_name = song_name
                
                # Try exact match first
                if song_key in musiclibrary.music:
                    found_url = musiclibrary.music[song_key]
                    found_song_name = song_key.replace("_", " ").title()
                else:
                    # Try partial match
                    for key in musiclibrary.music.keys():
                        if song_key in key or key in song_key:
                            found_url = musiclibrary.music[key]
                            found_song_name = key.replace("_", " ").title()
                            break
                
                if found_url:
                    # Song found in library - use direct video URL
                    action = "pending_action"
                    url = found_url
                    response = f"I found {found_song_name}. Click to play it."
                    print(f"✅ Found '{song_name}' in music library: {found_url}")
                    
                    return {
                        'response': response,
                        'action': action,
                        'url': url
                    }
                else:
                    # Song not in library - try Gemini if available
                    if google_api_key:
                        print(f"❌ '{song_name}' not in library, searching with Gemini...")
                        youtube_url = self._find_song_on_youtube(song_name)
                        if youtube_url:
                            # Determine if it's a direct video URL or search fallback
                            is_direct_video = 'watch?v=' in youtube_url
                            
                            action = "pending_action"
                            url = youtube_url
                            
                            if is_direct_video:
                                response = f"I found {song_name}. Click to play it."
                                print(f"✅ Found '{song_name}' via Gemini")
                            else:
                                response = f"Searching for {song_name} on YouTube"
                                print(f"📺 Using YouTube search for '{song_name}'")
                            
                            return {
                                'response': response,
                                'action': action,
                                'url': url
                            }
                        else:
                            response = f"No song found in my music library. Try another song or search manually."
                    else:
                        response = f"No song found in my music library. Please enable Google API for dynamic search."
        
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
        
        # Return dict with response and optional action/url
        return {
            'response': response,
            'action': action,
            'url': url
        }
    
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
    
    def _find_song_on_youtube(self, song_name):
        """Use Gemini to find a song on YouTube and return the video URL
        
        Returns a direct YouTube watch URL if found, otherwise returns a search URL.
        """
        try:
            if not google_api_key:
                # Fallback to search if no API key
                search_query = song_name.replace(" ", "+")
                return f"https://www.youtube.com/results?search_query={search_query}"
            
            print(f"🎵 Gemini: Searching for '{song_name}'...")
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # Improved prompt to get the most accurate result
            prompt = f"""Find the OFFICIAL or MOST POPULAR YouTube video for: "{song_name}"
            
Return ONLY the direct YouTube watch URL in this exact format:
https://www.youtube.com/watch?v=VIDEO_ID

Rules:
- Get the VIDEO_ID from the URL (the alphanumeric string after 'v=')
- Find official uploads, official audio tracks, or the most popular version
- Do NOT return search URLs, playlist URLs, or short URLs
- Return ONLY the URL, nothing else
- If you cannot find any result, respond with: SEARCH:{song_name}"""
            
            response = model.generate_content(prompt)
            result = response.text.strip()
            
            # Check if Gemini wants us to do a search instead
            if result.startswith("SEARCH:"):
                search_query = song_name.replace(" ", "+")
                fallback_url = f"https://www.youtube.com/results?search_query={search_query}"
                print(f"⚠️ Gemini: Falling back to search for '{song_name}'")
                return fallback_url
            
            # Validate it's a proper YouTube direct video URL
            if 'youtube.com' in result and 'watch?v=' in result:
                # Extract video ID to verify it's valid format
                if len(result.split('v=')[-1]) >= 10:  # YouTube video IDs are typically 11 chars
                    print(f"✅ Gemini: Found video for '{song_name}': {result}")
                    return result
            
            # If response doesn't look right, fall back to search
            search_query = song_name.replace(" ", "+")
            fallback_url = f"https://www.youtube.com/results?search_query={search_query}"
            print(f"⚠️ Gemini: Invalid response format, using search: {result[:50]}...")
            return fallback_url
            
        except Exception as e:
            print(f"❌ Gemini Song Search Error: {e}")
            # Fallback to YouTube search
            search_query = song_name.replace(" ", "+")
            return f"https://www.youtube.com/results?search_query={search_query}"
    
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
    result = assistant.process_command(command)
    
    # Handle new dict response format
    if isinstance(result, dict):
        response_text = result.get('response', '')
        action = result.get('action')
        url = result.get('url')
    else:
        # Backward compatibility with old string format
        response_text = result
        action = None
        url = None
    
    # Update state
    assistant_state['last_command'] = command
    assistant_state['last_response'] = response_text
    assistant_state['history'].append({
        'command': command,
        'response': response_text,
        'timestamp': datetime.now().isoformat()
    })
    
    # Keep only last 50 items
    if len(assistant_state['history']) > 50:
        assistant_state['history'] = assistant_state['history'][-50:]
    
    # Build response
    response_data = {
        'command': command,
        'response': response_text,
        'timestamp': datetime.now().isoformat()
    }
    
    # Add action and URL if present
    if action:
        response_data['action'] = action
    if url:
        response_data['url'] = url
    
    return jsonify(response_data)

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
