# 🚀 Replit Setup Guide - Real-Time Voice Translator

This guide will help you set up and run the Voice Translator application on Replit.

## Step-by-Step Setup Instructions

### 1. Create a New Replit Project

1. Go to [Replit.com](https://replit.com)
2. Click the **"Create"** button in the top-left
3. Select **"Python"** from the language options
4. Name your project (e.g., "voice-translator")
5. Click **"Create Repl"**

### 2. Upload Project Files

You have two options:

**Option A: Upload Files Directly**
1. Click the **"Upload file"** button (upload icon) in the Files panel
2. Select and upload:
   - `app.py`
   - `requirements.txt`
   - `config.py`
   - `README.md`

**Option B: Use Version Control (Git)**
1. In the shell, run:
   ```bash
   git clone <your-repository-url>
   cd multilingual-translator
   ```

### 3. Install Dependencies

In the Replit shell (right panel), run:

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit
- SpeechRecognition
- googletrans
- gTTS
- PyAudio (for audio I/O)

**Note**: PyAudio installation may take a few minutes on Replit. Please be patient.

### 4. Run the Application

In the Replit shell, run:

```bash
streamlit run app.py
```

### 5. Access Your App

After running the command, you'll see output like:
```
You can now view your Streamlit app in your browser.

URL: http://localhost:8501
```

Replit will automatically open the app in a split-screen view or you can click the webview panel.

## 🎤 Using Microphone in Replit

Replit provides audio input through the browser's WebRTC interface.

**Steps to Use Microphone:**
1. When you click "Start Recording", the browser may ask for microphone permission
2. **Allow** microphone access when prompted
3. The app will capture audio through your device's microphone
4. Speak clearly into your microphone

**Note**: Audio quality and connectivity depend on your internet connection.

## 📝 Troubleshooting for Replit

### Issue 1: "ModuleNotFoundError: No module named 'pyaudio'"

**Solution:**
- PyAudio may take time to install on Replit
- Try restarting the Repl: Click the 🔄 reload button
- If it persists, Replit's microphone interface will still work through Streamlit

### Issue 2: Microphone Not Detected

**Solution:**
1. Check browser permissions:
   - Click the 🔒 lock icon in the address bar
   - Ensure "Microphone" is set to "Allow"
2. Refresh the Replit page (Ctrl+R)
3. Try recording again

### Issue 3: "Connection Timeout" During Translation

**Solution:**
- Check your internet connection
- Wait a few seconds and try again
- Translation services may be temporarily unavailable

### Issue 4: Audio Doesn't Play

**Solution:**
1. Unmute your speakers
2. Check volume levels
3. Click the audio player's play button
4. Try a different browser

### Issue 5: Slow Response

**Solution:**
- This is normal on Replit due to server limitations
- The app is still processing; wait for the progress messages
- Consider running the app locally for faster performance

## 🔧 Customizing the Application

### Add More Languages

Edit the `LANGUAGE_MAP` in `app.py`:

```python
LANGUAGE_MAP = {
    "Telugu": "te",
    "Hindi": "hi",
    # Add more languages here:
    # "Portuguese": "pt",
    # "Russian": "ru",
    # "Japanese": "ja",
}
```

Language codes are ISO 639-1 codes. See full list [here](https://en.wikipedia.org/wiki/ISO_639-1).

### Adjust Recording Timeout

In `app.py`, line ~130, modify:

```python
audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
```

- `timeout`: Maximum time to wait for speech to start (seconds)
- `phrase_time_limit`: Maximum length of a single phrase (seconds)

### Change UI Colors

Edit the CSS section in `app.py` (lines ~30-40) to customize colors and styling.

## 📊 Performance Tips

1. **Keep Audio Short**: Record 10-30 seconds at a time
2. **Use Stable Internet**: Translation and TTS require internet
3. **Rest Between Recordings**: Give the API time to process
4. **Clear Cache**: If slow, refresh the page (Ctrl+R)

## 🔐 Privacy Notes

- Voice data is sent to Google for speech recognition
- Text is sent to Google Translate for translation
- Text is sent to Google TTS for audio generation
- No data is permanently stored by the app
- Replit logs may contain activity logs

## 🌐 Making Your App Public

To share your Replit app with others:

1. Click the **"Share"** button (top-right of Replit)
2. Enable **"Invite link"**
3. Share the generated URL with others
4. They can access and use your app directly

**Note**: For public apps, be aware of API usage limits from Google services.

## 💾 Saving Your Work

To save your Replit project:

1. Replit automatically saves files
2. To download files, right-click and select "Download"
3. To version control, connect to GitHub (see Replit documentation)

## 📞 Getting Help

If you encounter issues:

1. Check the error message in the terminal
2. Review the **Troubleshooting** section above
3. Check Replit's [Documentation](https://docs.replit.com)
4. Check Streamlit's [Documentation](https://docs.streamlit.io)

## 🎉 You're All Set!

Your Voice Translator app is now running on Replit! 

**Next Steps:**
- Try recording in different languages
- Test the translation quality
- Customize languages and settings
- Share your app with friends!

---

**Happy Translating! 🌍✨**
