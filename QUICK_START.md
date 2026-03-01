# ⚡ Quick Start Guide

Get your Voice Translator running in 5 minutes!

## 🚀 For Desktop/Local Machine

### 1. Install Python
- Download from [python.org](https://www.python.org/) (3.8+)
- During installation, ✅ check "Add Python to PATH"

### 2. Clone/Download Project
- Download the project files or git clone the repository
- Navigate to the project folder in terminal/command prompt

### 3. Run the App
**Windows:**
```bash
run.bat
```

**macOS/Linux:**
```bash
bash run.sh
```

**Manual (All Systems):**
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### 4. Use the App
- Browser opens automatically at `http://localhost:8501`
- Select language from dropdown
- Click **"🎤 Start Recording"**
- Speak clearly
- Listen to translation!

---

## 🌐 For Replit

### 1. Create New Repl
- Go to [Replit.com](https://replit.com)
- Click **"Create"** → Select **"Python"**

### 2. Upload Files
- Click upload icon
- Select: `app.py`, `requirements.txt`, `config.py`

### 3. Install & Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 4. Use the App
- Open in webview
- Allow microphone permission when asked
- Select language, click record, speak!

---

## 🎯 Basic Usage

1. **Select Language**: Choose from dropdown (Telugu, Hindi, French, Spanish, German, Marathi, Tamil, Kannada)
2. **Record**: Click blue button, speak for 10 seconds
3. **View Results**:
   - Original text (what was heard)
   - Translated text (in selected language)
   - Audio player (hear the translation)

---

## 📋 Requirements

- Python 3.8+
- Microphone
- Internet connection
- ~2 MB disk space
- ~200 MB for dependencies

---

## ⚠️ Common Issues

| Issue | Solution |
|-------|----------|
| Microphone not found | Check Settings → Sound → Input |
| "Could not understand audio" | Speak clearly, reduce background noise |
| Translation failed | Check internet, wait a moment, try again |
| No audio playback | Check volume, unmute browser notifications |
| Slow response | Normal (5-8 seconds). Check internet speed |

**More help?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📁 Key Files

- `app.py` - Main application
- `requirements.txt` - Dependencies to install
- `config.py` - Configuration & settings
- `README.md` - Full documentation
- `REPLIT_SETUP.md` - Replit-specific guide
- `TROUBLESHOOTING.md` - Problem solutions

---

## 🎓 What It Does

1. **Records** your voice from microphone (10 seconds max)
2. **Transcribes** speech to text using Google Speech Recognition
3. **Translates** text to selected language using Google Translate
4. **Converts** translated text to speech using Google TTS
5. **Plays** audio automatically for you to hear

---

## 🔧 Customization

### Change Default Language
Edit `app.py` line ~95:
```python
index=0,  # Change index (0=Telugu, 1=Hindi, etc)
```

### Add New Languages
Edit `app.py` line ~55:
```python
LANGUAGE_MAP = {
    "Turkish": "tr",      # Add this line
    "Japanese": "ja",     # Add this line
    # ... rest of languages
}
```

### Adjust Recording Time
Edit `app.py` line ~130:
```python
audio = recognizer.listen(source, timeout=15, phrase_time_limit=15)  # Increase to 15 seconds
```

---

## 🌍 Supported Languages

| Language | Code |
|----------|------|
| Telugu | te |
| Hindi | hi |
| French | fr |
| Spanish | es |
| German | de |
| Marathi | mr |
| Tamil | ta |
| Kannada | kn |

Need more languages? Find codes at [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)

---

## 💡 Tips for Best Results

✅ **DO:**
- Use a good microphone
- Speak clearly and naturally
- Use proper English pronunciation
- Test in quiet environments
- Keep sentences simple

❌ **DON'T:**
- Rush or mumble words
- Translate in very noisy places
- Use technical jargon or slang
- Record for more than 10 seconds at once
- Rely solely on translation (review results)

---

## 🎯 Next Steps

Once running:
1. Try different languages
2. Test with different sentences
3. Adjust settings in `app.py`
4. Share your app (Replit: click "Share")
5. Customize UI colors in `app.py` (lines 30-40)

---

## 📞 Need Help?

- 📖 See [README.md](README.md) for full documentation
- 🔧 See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for issues
- 🌐 See [REPLIT_SETUP.md](REPLIT_SETUP.md) for Replit help
- 🐙 Check GitHub issues or documentation links

---

## 🎉 You're All Set!

Your voice translator is ready to use. Enjoy translating! 🌍✨

**Questions?** Start with TROUBLESHOOTING.md or README.md
