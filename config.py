"""Configuration settings for Orion Voice Assistant"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini / Google API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
# Optional: model name for Gemini integration if used by `client.py`
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini")

# Using Google Gemini (Generative AI)
# Google / Gemini API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
# Optional: model name for Gemini integration if used by `client.py`
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini")

# Speech Recognition Settings
PHRASE_TIME_LIMIT = 5  # seconds
AMBIENT_NOISE_DURATION = 1  # seconds
WAKE_WORD_TIME_LIMIT = 3  # seconds

# Text-to-Speech Settings
TTS_LANGUAGE = "en"  # Language for text-to-speech

# Assistant Settings
ASSISTANT_NAME = "Orion"
TEMP_AUDIO_FILE = "temp.mp3"

# Logging Settings
LOG_FILE = "logs/orion.log"
LOG_LEVEL = "INFO"

# Weather API (optional - for future implementation)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")

# Feature Flags
# Use Gemini (Google) when `GOOGLE_API_KEY` is present or when `USE_GEMINI` is set
USE_GEMINI = os.getenv("USE_GEMINI", "true").lower() in ("1", "true", "yes") or bool(GOOGLE_API_KEY)

ENABLE_LOGGING = True
