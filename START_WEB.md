# 🚀 Quick Start - Web Interface

Get the Orion web interface running in 3 simple steps!

## Step 1: Install Flask

```bash
pip install Flask Flask-CORS
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

## Step 2: Start the Server

```bash
python app.py
```

You should see:
```
==================================================
🚀 Orion Voice Assistant Starting...
==================================================
🌐 Open your browser to: http://localhost:5000
✅ OpenAI: Enabled/Disabled
🎵 Songs available: 22
==================================================
```

## Step 3: Open Browser

Navigate to: **http://localhost:5000**

That's it! 🎉

## 🎤 Using the Interface

### Voice Input
1. Click the **microphone button** (🎤)
2. Speak your command
3. Wait for the response

### Text Input
1. Type in the input box
2. Press **Enter** or click **send** (➤)

### Quick Commands
Click any quick command button for instant actions:
- ⏰ Current Time
- 📅 Today's Date
- 🎵 List Songs
- 🌐 Open Google
- 🧮 Calculate

## 💡 Pro Tips

- **Voice works best in Chrome/Edge** browsers
- **Type commands** if voice isn't working
- **Use quick commands** for faster access
- **Check history** to reuse previous commands
- **Mobile friendly** - works on phones too!

## 🐛 Issues?

### Port Already in Use
```bash
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Microphone Not Working
- Allow microphone access in browser
- Use Chrome or Edge browser
- Check system microphone settings

### Can't Access from Phone
```bash
# Find your IP address
ipconfig

# Access using
http://YOUR_IP:5000
```

## 📚 Full Documentation

For detailed information, see:
- **WEB_INTERFACE.md** - Complete web interface guide
- **README.md** - Full project documentation
- **QUICKSTART.md** - General quick start

---

**Enjoy Orion! 🤖✨**
