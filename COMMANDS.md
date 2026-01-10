# 🎙️ Orion Voice Assistant - Complete Command List

This document contains **ALL commands** you can give to Orion, from start to finish.

---

## 📋 Table of Contents
1. [Time & Date Commands](#-time--date-commands)
2. [Music Commands](#-music-commands)
3. [Web Browsing Commands](#-web-browsing-commands)
4. [Information & Search](#-information--search)
5. [System Commands](#-system-commands)
6. [AI Commands (OpenAI)](#-ai-commands-openai)

---

## ⏰ Time & Date Commands

### Get Current Time
```
"What time is it?"
"Tell me the time"
"Current time"
"What's the time?"
```

### Get Current Date
```
"What is the date?"
"Tell me the date"
"What's today's date?"
"Today's date"
```

---

## 🎵 Music Commands

### Play Songs
Play any of the 20 available songs by name:

**English Songs:**
```
"Play blinding lights"
"Play shape of you"
"Play perfect"
"Play believer"
"Play bad guy"
"Play faded"
"Play senorita"
"Play drivers license"
"Play levitating"
"Play dance monkey"
```

**Hindi Songs:**
```
"Play kesariya"
"Play tum hi ho"
"Play shayad"
"Play levi ki adi"
"Play dil bechara"
"Play raabta"
```

**Kannada Songs:**
```
"Play rajeev shetty"
"Play karna nadu"
"Play hebbuli song"
"Play anjanappa song"
```

### List All Songs
```
"Show songs"
"List all songs"
"What songs do you have?"
"Show me the music library"
```

---

## 🌐 Web Browsing Commands

### Open Websites
```
"Open Google"
"Open YouTube"
"Open Facebook"
"Open LinkedIn"
```

**Note:** These commands open websites in a new browser tab.

---

## 📚 Information & Search

### Wikipedia Search
Ask Orion about any topic and it will search Wikipedia:

```
"What is artificial intelligence?"
"Tell me about Python programming"
"What is machine learning?"
"Search for Elon Musk"
"Tell me about the Taj Mahal"
```

**Format:** Just ask "What is [topic]?" or "Tell me about [topic]"

---

## 🔧 System Commands

### Exit Orion (Console Version Only)
```
"Exit Orion"
"Quit"
"Goodbye"
"Stop"
```

**Note:** In the web interface, just close the browser tab.

---

## 🤖 AI Commands (OpenAI)

**Requirements:** You need to add your OpenAI API key in the `.env` file.

### General Conversations
Once OpenAI is enabled, you can have natural conversations:

```
"Write a poem about nature"
"Explain quantum physics in simple terms"
"Give me a recipe for chocolate cake"
"Tell me a joke"
"What's the meaning of life?"
```

**How to Enable:**
1. Create a `.env` file in the project root
2. Add: `OPENAI_API_KEY=your_api_key_here`
3. Restart the application

---

## 💡 Usage Tips

### Voice Input
1. Click the **cyan microphone button** 🎤
2. Wait for "Listening..." status
3. Speak your command clearly
4. Wait for Orion's response

### Text Input
1. Click the **keyboard button** ⌨️
2. Type your command
3. Press **Enter** or click **Send**
4. Input box auto-closes after sending

### Click Outside to Close
- Click anywhere outside the text input box to close it

---

## 📝 Command Examples

### Quick Time Check
```
User: "What time is it?"
Orion: "The current time is 2:30 PM"
```

### Play Music
```
User: "Play perfect"
Orion: "Playing Perfect by Ed Sheeran" (opens YouTube)
```

### Search Wikipedia
```
User: "What is Python?"
Orion: "According to Wikipedia, Python is a high-level programming language..."
```

### Open Website
```
User: "Open Google"
Orion: "Opening Google" (opens google.com in new tab)
```

---

## 🎯 Best Practices

### ✅ DO:
- Speak clearly and at normal speed
- Use simple, direct commands
- Say the exact song name for music
- Allow microphone access when prompted

### ❌ DON'T:
- Don't speak too fast or too slow
- Don't use complex sentence structures
- Don't expect commands not listed here to work
- Don't forget to enable OpenAI for AI features

---

## 🔍 Command Categories Summary

| Category | Number of Commands | Examples |
|----------|-------------------|----------|
| **Time & Date** | 8+ variations | "What time is it?" |
| **Music** | 20 songs | "Play perfect" |
| **Web** | 4 websites | "Open Google" |
| **Search** | Unlimited | "What is [topic]?" |
| **System** | 4 commands | "Exit Orion" |
| **AI Chat** | Unlimited* | Any conversation |

*Requires OpenAI API key

---

## 📊 Available Songs List

### English (10 songs)
1. Blinding Lights - The Weeknd
2. Shape of You - Ed Sheeran
3. Perfect - Ed Sheeran
4. Believer - Imagine Dragons
5. Bad Guy - Billie Eilish
6. Faded - Alan Walker
7. Senorita - Shawn Mendes, Camila Cabello
8. Drivers License - Olivia Rodrigo
9. Levitating - Dua Lipa
10. Dance Monkey - Tones and I

### Hindi (6 songs)
1. Kesariya - Brahmastra
2. Tum Hi Ho - Aashiqui 2
3. Shayad - Love Aaj Kal
4. Levi Ki Adi - Khiladi 786
5. Dil Bechara - Dil Bechara
6. Raabta - Agent Vinod

### Kannada (4 songs)
1. Rajeev Shetty Song
2. Karna Nadu
3. Hebbuli Song
4. Anjanappa Song

---

## 🆘 Troubleshooting Commands

### If Voice Recognition Fails:
1. Check browser console (F12) for errors
2. Ensure microphone permission is granted
3. Use **text input** as alternative (keyboard button)
4. Try refreshing the page

### If Song Won't Play:
- Make sure you say the exact song name
- Try typing it instead of voice
- Check console logs for debugging info

### If OpenAI Doesn't Work:
- Verify `.env` file exists
- Check API key is correct
- Restart the Flask server

---

## 🎓 Advanced Usage

### Chaining Commands
You can give multiple commands one after another:

```
1. "What time is it?"
2. Wait for response
3. "Open YouTube"
4. Wait for response
5. "Play perfect"
```

### Custom Variations
Most commands accept natural variations:

**Time:**
- "What's the time?" ✅
- "Time please" ✅
- "Current time" ✅

**Music:**
- "Play perfect" ✅
- "Play the song perfect" ✅
- "I want to hear perfect" ✅

---

## 📞 Need More Features?

Want to add more commands? Check out:
- `main.py` - Main command processing logic
- `musiclibrary.py` - Add more songs here
- `app.py` - Web interface API
- `client.py` - OpenAI integration

---

## 🎉 Quick Reference Card

### Most Common Commands:
```
⏰ "What time is it?"
📅 "What is the date?"
🎵 "Show songs"
🎵 "Play [song name]"
🌐 "Open Google"
📚 "What is [topic]?"
🤖 [Any question with OpenAI enabled]
```

---

**Developer:** Charan Kumar  
**GitHub:** https://github.com/charan-kumar99  
**Version:** 1.0  
**Last Updated:** October 2025

---

💡 **Tip:** Bookmark this file for quick reference while using Orion!
