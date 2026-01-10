import speech_recognition as sr
import webbrowser
import wikipedia
import musiclibrary
from gtts import gTTS
import pygame
import os
import time
import sys
import logging
import re
from datetime import datetime
import config
from client import get_ai_response

# Initialize pygame mixer
pygame.mixer.init()

# Setup logging
if config.ENABLE_LOGGING:
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename=config.LOG_FILE,
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
else:
    logger = None

def speak(text):
    """Speak text aloud using gTTS + pygame and print formatted output"""
    print(f"🤖 {config.ASSISTANT_NAME}: {text}")
    if logger:
        logger.info(f"Assistant: {text}")
    
    try:
        tts = gTTS(text, lang=config.TTS_LANGUAGE)
        tts.save(config.TEMP_AUDIO_FILE)
        pygame.mixer.music.load(config.TEMP_AUDIO_FILE)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        
        # Clean up temp file
        if os.path.exists(config.TEMP_AUDIO_FILE):
            os.remove(config.TEMP_AUDIO_FILE)
    except Exception as e:
        print(f"Speech Error: {e}")
        if logger:
            logger.error(f"Speech error: {e}")

def get_greeting():
    """Return a greeting based on the current time"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Hello"

def search_wikipedia(query):
    """Search Wikipedia and speak the result"""
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
        if logger:
            logger.info(f"Wikipedia search: {query}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"There are multiple results for {query}. Please be more specific.")
        if logger:
            logger.warning(f"Wikipedia disambiguation for: {query}")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find anything on Wikipedia for that query.")
        if logger:
            logger.warning(f"Wikipedia page not found: {query}")
    except Exception as e:
        print(f"Wiki Error: {e}")
        speak("Sorry, I encountered an error searching Wikipedia.")
        if logger:
            logger.error(f"Wikipedia error: {e}")

def get_current_time():
    """Get and speak the current time"""
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    speak(f"The time is {time_str}")

def get_current_date():
    """Get and speak the current date"""
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")
    speak(f"Today is {date_str}")

def calculate(expression):
    """Perform basic mathematical calculations"""
    try:
        # Remove 'calculate' or 'what is' from the expression
        expression = re.sub(r'(calculate|what is|whats)', '', expression, flags=re.IGNORECASE).strip()
        
        # Replace word operators with symbols
        expression = expression.replace('plus', '+').replace('minus', '-')
        expression = expression.replace('times', '*').replace('multiplied by', '*')
        expression = expression.replace('divided by', '/').replace('divide', '/')
        
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        speak(f"The answer is {result}")
        if logger:
            logger.info(f"Calculation: {expression} = {result}")
    except Exception as e:
        speak("Sorry, I couldn't perform that calculation.")
        if logger:
            logger.error(f"Calculation error: {e}")

def processCommand(command):
    """Process and execute user commands"""
    command = command.lower()
    
    if logger:
        logger.info(f"Processing command: {command}")

    # Exit command
    if "exit" in command or "quit" in command or "bye" in command:
        speak("Shutting down. Goodbye!")
        sys.exit(0)

    # Show available songs
    elif "show songs" in command or "list songs" in command:
        speak("Here are the available songs:")
        for i, song in enumerate(musiclibrary.music.keys(), 1):
            song_name = song.replace("_", " ").title()
            print(f"{i}. {song_name}")
        return

    # Time and date
    elif "time" in command:
        get_current_time()
    elif "date" in command or "today" in command:
        get_current_date()

    # Calculations
    elif "calculate" in command or ("what" in command and any(op in command for op in ["plus", "minus", "times", "divided", "+", "-", "*", "/"])):
        calculate(command)

    # Web browsing
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif "open" in command and ".com" in command:
        # Extract website name
        website = command.replace("open", "").strip()
        if not website.startswith("http"):
            website = f"https://{website}"
        speak(f"Opening {website}")
        webbrowser.open(website)

    # Music playback
    elif command.startswith("play"):
        song_name = command.replace("play", "").strip().lower().replace(" ", "_")
        if song_name in musiclibrary.music:
            speak(f"Playing {song_name.replace('_', ' ')}")
            webbrowser.open(musiclibrary.music[song_name])
        else:
            speak("Sorry, I don't have that song in my library.")

    # Wikipedia search or AI response
    else:
        # Try AI response first if available
        if config.USE_GEMINI:
            speak("Let me think about that...")
            ai_response = get_ai_response(command)
            if ai_response:
                speak(ai_response)
                return
        
        # Fall back to Wikipedia
        speak(f"Searching Wikipedia for {command}")
        search_wikipedia(command)

# Main loop
if __name__ == "__main__":
    print("="*50)
    print(f"🚀 {config.ASSISTANT_NAME} Voice Assistant Starting...")
    print("="*50)
    
    if config.USE_GEMINI:
        print("✅ Gemini integration enabled")
    else:
        print("ℹ️  Gemini integration disabled (no API key)")
    
    greeting = get_greeting()
    startup_message = f"{greeting}! I am {config.ASSISTANT_NAME}, your voice assistant. Say '{config.ASSISTANT_NAME}' to wake me up."
    speak(startup_message)
    
    if logger:
        logger.info(f"{config.ASSISTANT_NAME} started successfully")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("\n🎤 Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=config.AMBIENT_NOISE_DURATION)
                audio = recognizer.listen(source, phrase_time_limit=config.WAKE_WORD_TIME_LIMIT)

                try:
                    word = recognizer.recognize_google(audio)
                    print(f"🧑 You said: {word}")

                    if config.ASSISTANT_NAME.lower() in word.lower():
                        speak("Yes? How can I help you?")

                        time.sleep(0.5)

                        with sr.Microphone() as source2:
                            recognizer.adjust_for_ambient_noise(source2, duration=0.5)
                            print("🎤 Listening for your command...")
                            audio2 = recognizer.listen(source2, phrase_time_limit=config.PHRASE_TIME_LIMIT)

                            try:
                                command = recognizer.recognize_google(audio2)
                                print(f"🧑 Command: {command}")
                                processCommand(command)
                            except sr.UnknownValueError:
                                speak("Sorry, I did not catch that. Could you repeat?")
                            except sr.RequestError:
                                speak("Sorry, there was an error with the speech recognition service.")
                            except Exception as e:
                                print(f"Command Error: {e}")
                                speak("Sorry, I encountered an error processing your command.")

                except sr.UnknownValueError:
                    pass  # Ignore background noise
                except sr.RequestError as e:
                    print(f"Speech Recognition Error: {e}")
                    if logger:
                        logger.error(f"Speech recognition error: {e}")
                except Exception:
                    pass  # Ignore other audio errors

        except KeyboardInterrupt:
            print("\n\n👋 Keyboard interrupt detected")
            speak("Shutting down. Goodbye!")
            if logger:
                logger.info(f"{config.ASSISTANT_NAME} shut down by user")
            break
        except Exception as e:
            print(f"System Error: {e}")
            if logger:
                logger.error(f"System error: {e}")
            time.sleep(1)
