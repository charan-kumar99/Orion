# 🤖 Orion - Your Personal Voice Assistant

Orion is an intelligent voice-activated personal assistant built with Python, similar to Alexa or Google Assistant. It responds to voice commands and can perform various tasks like opening websites, playing music, searching Wikipedia, and more.

## ✨ Features

### Core Features
- 🎤 **Voice Activation**: Wake up Orion with the wake word "Orion"
- 🗣️ **Text-to-Speech**: Natural voice responses using Google Text-to-Speech
- 🌐 **Web Browsing**: Open popular websites (Google, YouTube, Facebook, LinkedIn)
- 🎵 **Music Player**: Play songs from a curated library via YouTube
- 📚 **Wikipedia Search**: Get information on any topic
- 🤖 **AI Integration**: Google Gemini-powered intelligent responses (optional)
- ⏰ **Time & Date**: Get current time and date information
- 🧮 **Calculations**: Perform basic mathematical calculations

### 🌐 Web Interface (NEW!)
- **Beautiful Browser-Based UI**: Modern, responsive web interface
- **Voice & Text Input**: Type or speak your commands
- **Real-time Chat**: Interactive conversation display
- **Quick Commands**: One-click access to common tasks
- **Command History**: Track and reuse previous commands
- **Interactive Animations**: Dynamic Orb with wave-text effects
- **Letter Wave Status**: Staggered animation for status text
- **Cross-Platform**: Works on any device with a browser

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Microphone access
- Internet connection

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Orion
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

### Running Orion

**Console Version (Voice-activated):**
```bash
python main.py
```

**Web Interface (Browser-based):**
```bash
python app.py
```
Then open your browser to: http://localhost:5000

> 💡 **Tip**: The web interface is recommended for easier interaction and better user experience!

## 🎯 Usage

1. **Wake up Orion**: Say "Orion" to activate the assistant
2. **Give commands**: After Orion responds, say your command

### Example Commands

- "Open Google"
- "Open YouTube"
- "Play blinding lights"
- "Show songs"
- "What time is it"
- "What is artificial intelligence" (searches Wikipedia)
- "Exit Orion" (to quit)

## 📁 Project Structure

```
Orion/
├── main.py              # Console voice assistant
├── app.py               # Flask web server (NEW!)
├── client.py            # OpenAI API integration
├── musiclibrary.py      # Song database
├── config.py            # Configuration settings
├── utils.py             # Utility functions
├── setup.py             # Setup automation
├── test_features.py     # Testing suite
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates (NEW!)
│   └── index.html       # Web interface UI
├── static/              # Static assets (NEW!)
│   ├── style.css        # Styling
│   └── app.js           # Frontend JavaScript
├── logs/                # Log files
├── .env                 # Environment variables (create this)
├── .gitignore           # Git ignore rules
├── README.md            # Main documentation
├── QUICKSTART.md        # Quick start guide
├── WEB_INTERFACE.md     # Web interface docs (NEW!)
└── IMPROVEMENTS.md      # Change log
```

## 🛠️ Configuration

Edit `config.py` to customize:
- Speech recognition settings
- Response timeout durations
- Default language
- API endpoints

## 🔒 Security

- Never commit your `.env` file or API keys to version control
- The `.env` file is included in `.gitignore` for security

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google Speech Recognition API
- Google Text-to-Speech (gTTS)
- Google Gemini API
- Wikipedia API
- Pygame for audio playback

## 🐛 Troubleshooting

### Microphone Issues
- Ensure your microphone is connected and working
- Check system permissions for microphone access

### Speech Recognition Errors
- Speak clearly and avoid background noise
- Adjust the `phrase_time_limit` in the code if needed

### Audio Playback Issues
- Make sure pygame is properly installed
- Check system audio settings

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ by the Orion Team**
