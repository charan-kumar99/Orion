# 🚀 Quick Start Guide for Orion

Get Orion up and running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Note for PyAudio (Windows)
If you encounter errors installing PyAudio, download the appropriate wheel file:
1. Visit: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
2. Download the wheel matching your Python version
3. Install: `pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl`

## Step 2: Run Setup Script

```bash
python setup.py
```

This will:
- Create necessary directories (logs, cache)
- Create `.env` file from template
- Check if all dependencies are installed

## Step 3: Configure API Keys (Optional)

Edit the `.env` file and add your API keys:

```
OPENAI_API_KEY=your_key_here
```

**Note:** OpenAI integration is optional. Orion works without it using Wikipedia fallback.

## Step 4: Test Your Setup

Run the test script to verify everything works:

```bash
python test_features.py
```

## Step 5: Start Orion!

```bash
python main.py
```

## 🎤 Using Orion

1. **Wake up Orion**: Say "Orion"
2. **Wait for response**: Orion will say "Yes? How can I help you?"
3. **Give your command**: Speak your request clearly

### Example Commands

| Command | What it does |
|---------|-------------|
| "What time is it" | Tells current time |
| "What is the date" | Tells current date |
| "Open Google" | Opens Google in browser |
| "Play blinding lights" | Plays the song |
| "Show songs" | Lists available songs |
| "Calculate 25 plus 17" | Does math |
| "What is Python" | Searches Wikipedia |
| "Exit" or "Quit" | Closes Orion |

## 📝 Customization

### Change Assistant Name
Edit `config.py`:
```python
ASSISTANT_NAME = "YourNameHere"
```

### Add More Songs
Edit `musiclibrary.py` and add entries:
```python
"song_name": "https://youtube.com/watch?v=VIDEO_ID"
```

### Adjust Speech Recognition
In `config.py`:
```python
PHRASE_TIME_LIMIT = 5  # Increase if commands get cut off
AMBIENT_NOISE_DURATION = 1  # Adjust for noisy environments
```

## 🐛 Troubleshooting

### Microphone Not Working
- Check system settings for microphone permissions
- Test microphone in other applications first
- Try adjusting `AMBIENT_NOISE_DURATION` in config

### Speech Recognition Errors
- Ensure stable internet connection (Google Speech API requires internet)
- Speak clearly and reduce background noise
- Check microphone position and quality

### Module Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### OpenAI Not Working
- Verify API key in `.env` file
- Check API key is valid at https://platform.openai.com/api-keys
- Ensure you have API credits

## 🎯 Tips for Best Experience

1. **Speak Clearly**: Pronounce words distinctly
2. **Reduce Background Noise**: Use in quiet environment
3. **Wait for Prompt**: Let Orion acknowledge before speaking
4. **Use Short Commands**: Keep commands concise and clear
5. **Check Logs**: View `logs/orion.log` for debugging

## 📚 Learn More

- Full documentation: See `README.md`
- Configuration options: See `config.py`
- Add custom features: See `main.py` and `client.py`

## 🎉 You're Ready!

Enjoy using Orion! Say "Orion" and start exploring.

---

**Need Help?** Check the logs in `logs/orion.log` or open an issue on GitHub.
