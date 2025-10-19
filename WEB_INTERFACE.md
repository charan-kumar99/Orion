# 🌐 Orion Web Interface Documentation

The Orion Voice Assistant now includes a beautiful, modern web interface that you can access from any browser!

## ✨ Features

### 🎤 Voice Input
- **Browser-based voice recognition** using Web Speech API
- Click the microphone button and speak your command
- Works in Chrome, Edge, and other Chromium-based browsers

### ⌨️ Text Input
- Type commands directly into the input field
- Press Enter or click the send button
- Full keyboard support

### 🗣️ Voice Output
- Automatic text-to-speech responses
- Uses browser's native speech synthesis
- Clear, natural-sounding voice

### ⚡ Quick Commands
- Pre-configured buttons for common tasks
- One-click access to frequently used commands
- Customizable command shortcuts

### 📊 Real-time Status
- See OpenAI integration status
- View total songs available
- Monitor assistant activity

### 📜 Command History
- View recent commands and responses
- Click history items to reuse commands
- Clear history with one click

## 🚀 Getting Started

### 1. Install Dependencies

Make sure you have Flask and Flask-CORS installed:

```bash
pip install -r requirements.txt
```

### 2. Start the Web Server

```bash
python app.py
```

### 3. Open in Browser

Navigate to: **http://localhost:5000**

You should see the Orion web interface!

## 🎯 Using the Web Interface

### Voice Commands

1. **Click the microphone button** (🎤)
2. **Speak your command** clearly
3. **Wait for the response** - it will appear in the chat and be spoken aloud

### Text Commands

1. **Type your command** in the input box
2. **Press Enter** or click the send button (➤)
3. **View the response** in the chat area

### Quick Actions

Use the quick action buttons for instant commands:

- **⏰ Current Time** - Get the current time
- **📅 Today's Date** - Get today's date
- **🎵 List Songs** - Show available songs
- **🌐 Open Google** - Opens Google in a new tab
- **🧮 Calculate** - Perform calculations

## 📱 Interface Overview

### Main Chat Area
- **Left side**: Large chat interface showing conversation history
- **User messages**: Displayed on the right in blue
- **Assistant responses**: Displayed on the left with robot avatar
- **Auto-scroll**: Automatically scrolls to latest message

### Right Sidebar

**Status Panel**
- OpenAI integration status
- Total songs in library

**Quick Commands Panel**
- Pre-configured command buttons
- Click any button to execute instantly

**History Panel**
- Last 10 commands
- Click to reuse a command
- Clear button to reset history

## 🎨 Customization

### Change Assistant Name

The web interface automatically uses the name from `config.py`:

```python
ASSISTANT_NAME = "YourName"
```

### Modify Quick Commands

Edit `templates/index.html` to add/remove quick command buttons:

```html
<button class="command-item" onclick="sendQuickCommand('Your command here')">
    <span class="cmd-icon">🎯</span>
    <span>Your Label</span>
</button>
```

### Customize Colors

Edit `static/style.css` to change the color scheme:

```css
:root {
    --primary-color: #6366f1;  /* Change to your preferred color */
    --secondary-color: #8b5cf6;
    /* ... more colors ... */
}
```

## 🌐 Browser Compatibility

### Fully Supported
- ✅ **Chrome** (recommended)
- ✅ **Microsoft Edge**
- ✅ **Brave**
- ✅ **Opera**

### Partially Supported
- ⚠️ **Firefox** (no Web Speech API - text input only)
- ⚠️ **Safari** (limited speech recognition)

### Not Supported
- ❌ Internet Explorer

## 🔧 Configuration

### Port Configuration

Change the port in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

### Enable Debug Mode

Debug mode is enabled by default for development:

```python
app.run(debug=True)  # Set to False for production
```

### API Endpoints

The web interface communicates with these endpoints:

- `GET /` - Main interface
- `GET /api/status` - Get assistant status
- `POST /api/process` - Process a command
- `POST /api/tts` - Text-to-speech conversion
- `GET /api/songs` - Get song library
- `GET /api/history` - Get command history
- `POST /api/clear-history` - Clear history

## 🛠️ Advanced Usage

### Running on Different Network

To access from other devices on your network:

1. Find your local IP address (e.g., 192.168.1.100)
2. Run the server:
   ```bash
   python app.py
   ```
3. Access from other devices:
   ```
   http://192.168.1.100:5000
   ```

### Production Deployment

For production use, consider:

1. **Use a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Set up HTTPS** using a reverse proxy (nginx/Apache)

3. **Disable debug mode** in `app.py`

4. **Set proper CORS policies** for security

## 🎯 Example Commands

Try these commands in the web interface:

### Time & Date
- "What time is it?"
- "What's today's date?"

### Calculations
- "Calculate 25 plus 17"
- "What is 100 divided by 4?"

### Information
- "What is artificial intelligence?"
- "Tell me about Python programming"

### Music
- "Show songs"
- "Play blinding lights"
- "Play shape of you"

### Web Browsing
- "Open Google"
- "Open YouTube"
- "Open github.com"

### AI Queries (if OpenAI enabled)
- "Explain quantum computing"
- "Write a short poem"
- "What are the benefits of exercise?"

## 🐛 Troubleshooting

### Microphone Not Working

**Issue**: Voice button not responding

**Solutions**:
1. Check browser permissions (allow microphone access)
2. Use Chrome/Edge for best compatibility
3. Check if microphone is connected and working
4. Look for permission prompt in address bar

### Connection Refused

**Issue**: Cannot access http://localhost:5000

**Solutions**:
1. Ensure server is running (`python app.py`)
2. Check if port 5000 is already in use
3. Try a different port
4. Check firewall settings

### Speech Recognition Not Available

**Issue**: Microphone button disabled

**Solutions**:
1. Use a compatible browser (Chrome/Edge)
2. Enable HTTPS (required for some browsers)
3. Fall back to text input

### No Audio Output

**Issue**: Not hearing responses

**Solutions**:
1. Check system volume
2. Verify browser has audio permissions
3. Check browser audio settings
4. Try refreshing the page

## 📊 Performance Tips

1. **Limit history size** - History stored in memory
2. **Close unused tabs** - Each connection uses resources
3. **Use local deployment** - Faster than network access
4. **Clear browser cache** if experiencing issues

## 🔒 Security Considerations

1. **Do not expose to public internet** without proper security
2. **Use environment variables** for API keys
3. **Enable authentication** for production use
4. **Set proper CORS policies**
5. **Use HTTPS** in production

## 🎉 Tips for Best Experience

1. **Speak clearly** when using voice input
2. **Wait for response** before next command
3. **Use quick commands** for faster access
4. **Check history** to reuse commands
5. **Keep browser tab active** for best performance

## 📚 Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- Web Speech API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API
- Orion Main README: See `README.md`
- Quick Start Guide: See `QUICKSTART.md`

---

**Enjoy using the Orion Web Interface! 🚀**
