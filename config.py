"""Configuration settings for Orion Voice Assistant"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-3.5-turbo"

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
USE_OPENAI = bool(OPENAI_API_KEY)  # Enable OpenAI only if API key is set
ENABLE_LOGGING = True
