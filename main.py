import speech_recognition as sr
import webbrowser
import wikipedia
import musiclibrary  # make sure this exists with song links
from gtts import gTTS
import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

def speak(text):
    """Speak text aloud using gTTS + pygame"""
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop and unload before removing file
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def search_wikipedia(query):
    """Search Wikipedia and speak the result"""
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        speak(summary)
    except:
        speak("Sorry, I could not find anything on Wikipedia.")

def processCommand(command):
    command = command.lower()

    if "exit orion" in command:
        speak("Shutting down. Goodbye!")
        exit()

    if "show songs" in command:
        speak("Here are the available songs:")
        for song in musiclibrary.music.keys():
            speak(song.replace("_", " "))
        return

    if "open google" in command:
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

    elif command.startswith("play"):
        song_name = command.replace("play ", "").strip()
        if song_name in musiclibrary.music:
            speak(f"Playing {song_name.replace('_',' ')}")
            webbrowser.open(musiclibrary.music[song_name])
        else:
            speak("Sorry, I don't have that song.")
    else:
        speak("Searching on Wikipedia...")
        search_wikipedia(command)

# Main loop
if __name__ == "__main__":
    speak("Initializing Orion...")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Orion'...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, phrase_time_limit=3)

                try:
                    word = recognizer.recognize_google(audio)
                    print(f"You said: {word}")

                    if "orion" in word.lower():  # Wake word detected
                        # Speak wake word response
                        speak("How can I help you?")

                        # Short pause
                        time.sleep(0.5)

                        # Listen for the command
                        with sr.Microphone() as source2:
                            recognizer.adjust_for_ambient_noise(source2, duration=0.5)
                            print("Listening for your command...")
                            audio2 = recognizer.listen(source2, phrase_time_limit=5)

                            try:
                                command = recognizer.recognize_google(audio2)
                                print(f"Command: {command}")
                                processCommand(command)
                            except:
                                speak("Sorry, I did not catch that.")

                except:
                    pass  # ignore background noise

        except KeyboardInterrupt:
            speak("Shutting down. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)
