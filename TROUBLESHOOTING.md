# 🔧 Troubleshooting Guide & FAQ

## Table of Contents
1. [Installation Issues](#installation-issues)
2. [Microphone Problems](#microphone-problems)
3. [Speech Recognition Issues](#speech-recognition-issues)
4. [Translation Problems](#translation-problems)
5. [Audio Playback Issues](#audio-playback-issues)
6. [Performance Issues](#performance-issues)
7. [Replit-Specific Issues](#replit-specific-issues)
8. [General FAQ](#general-faq)

---

## Installation Issues

### ❌ "ModuleNotFoundError: No module named 'streamlit'"

**Cause**: Streamlit is not installed in your environment.

**Solution**:
```bash
pip install streamlit==1.28.1
```

Or reinstall all dependencies:
```bash
pip install -r requirements.txt
```

---

### ❌ "ModuleNotFoundError: No module named 'pyaudio'"

**Cause**: PyAudio is not installed or failed to compile.

**Solution (Windows)**:
```bash
pip install pipwin
pipwin install pyaudio
```

**Solution (macOS)**:
```bash
brew install portaudio
pip install pyaudio
```

**Solution (Linux)**:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**Alternative for Replit**:
- If PyAudio fails to install, Replit still provides audio support through the browser
- The app will work without PyAudio on Replit

---

### ❌ "pip: command not found"

**Cause**: Python or pip is not installed.

**Solution**:
1. Install Python 3.8+ from [python.org](https://www.python.org/)
2. Verify installation:
   ```bash
   python --version
   pip --version
   ```

---

### ❌ Virtual Environment Activation Fails

**Solution (Windows)**:
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**Solution (macOS/Linux)**:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Microphone Problems

### ❌ "OSError: Microphone not found"

**Cause**: Microphone is not detected by the system.

**Solution**:
1. **Check hardware**: Ensure microphone is connected and powered
2. **Check system settings**:
   - Windows: Settings → Sound → Input
   - macOS: System Preferences → Sound → Input
   - Linux: Check with `pactl list sources`
3. **Test microphone**:
   ```bash
   python -m speech_recognition
   ```
4. **Reinstall PyAudio**:
   ```bash
   pip uninstall pyaudio
   pip install pyaudio
   ```
5. **Try different USB ports**: Sometimes changing USB ports helps

---

### ❌ "Microphone permission denied"

**Cause**: The app doesn't have microphone permissions.

**Solution (Windows)**:
1. Settings → Privacy & Security → Microphone
2. Ensure "Allow apps to access your microphone" is ON
3. Add Python or browser to allowed apps

**Solution (macOS)**:
1. System Preferences → Security & Privacy → Microphone
2. Add your terminal/IDE to the allowed apps list

**Solution (Linux)**:
```bash
# Check group membership
groups $USER
# Add user to audio group if needed
sudo usermod -aG audio $USER
# Log out and back in
```

---

### ❌ No sound input detected even with microphone connected

**Solution**:
1. Test microphone in another application
2. Check volume levels (not muted)
3. Try a different microphone if available
4. Update audio drivers
5. Restart the application

---

## Speech Recognition Issues

### ❌ "Could not understand audio"

**Cause**: Speech was not clear enough for recognition.

**Solutions**:
1. **Speak more clearly**: Articulate words distinctly
2. **Speak at normal pace**: Don't rush or speak too slowly
3. **Reduce background noise**: Find a quiet location
4. **Get closer to microphone**: Speak 6-12 inches from mic
5. **Use shorter sentences**: Break messages into segments
6. **Check microphone quality**: Test with another device

---

### ❌ "Error accessing Google Speech Recognition service"

**Cause**: No internet connection or API service is down.

**Solution**:
1. Check internet connection:
   ```bash
   ping 8.8.8.8
   ```
2. Check if Google services are accessible:
   - Open https://www.google.com in browser
3. Wait a few minutes and retry (service may be temporarily down)
4. Try with a VPN if Google services are blocked in your region

---

### ❌ Recording times out without capturing speech

**Cause**: Microphone not detecting sound or threshold too high.

**Solution**:
1. Speak louder or closer to microphone
2. Try in a quieter environment
3. Test microphone with: `python -m speech_recognition`
4. In `app.py`, adjust timeout settings (lines ~130):
   ```python
   # Increase timeout if your speech is slow
   audio = recognizer.listen(source, timeout=15, phrase_time_limit=15)
   ```

---

## Translation Problems

### ❌ "Translation failed"

**Cause**: Google Translate API error or no internet.

**Solution**:
1. Check internet connection
2. Try again after a few seconds
3. The Google Translate API has rate limits:
   - If translating too frequently, wait a minute
4. Try with a different sentence or language pair

---

### ❌ "HTTPError: 429 Too Many Requests"

**Cause**: Too many translation requests in a short time.

**Solution**:
1. Wait 1-2 minutes before translating again
2. Reduce frequency of requests
3. The library will eventually recover automatically

---

### ❌ Translation is inaccurate or nonsensical

**Cause**: Google Translate may misinterpret the original text.

**Solutions**:
1. Ensure speech recognition captured the text correctly
2. Use simpler, clearer language
3. Some language pairs may have lower accuracy
4. Try breaking your message into smaller parts

---

## Audio Playback Issues

### ❌ "No sound when playing translated audio"

**Cause**: Multiple possible reasons.

**Solutions**:
1. **Check volume**:
   - Computer volume not muted
   - Application volume not muted
   - Device volume not muted
2. **Check speakers**: 
   - Ensure speakers/headphones are connected
   - Try different audio output device
3. **Verify audio generation**:
   - Check if audio player appears in the UI
   - Try playing a different translation
4. **Browser audio**:
   - Unmute browser notifications
   - Check browser audio settings

---

### ❌ "Audio player doesn't appear"

**Cause**: Audio generation failed or not completed.

**Solution**:
1. Check console for error messages
2. Verify translation completed successfully
3. Try a simpler sentence
4. Refresh the page and try again

---

### ❌ Audio plays but too fast or too slow

**Cause**: gTTS speed setting or browser playback.

**Solution**:
1. In `app.py`, find the `convert_text_to_speech()` function
2. Adjust the `slow` parameter:
   ```python
   tts = gTTS(text=text, lang=language_code, slow=True)  # slow=True for slower audio
   tts = gTTS(text=text, lang=language_code, slow=False) # slow=False for faster audio
   ```

---

## Performance Issues

### ❌ App is running very slowly

**Cause**: Multiple factors (network, API response, processing).

**Solutions**:
1. **Check internet speed**:
   - Test at speedtest.net
   - Need at least 2 Mbps for reliable operation
2. **Check system resources**:
   - Close other applications
   - Check RAM usage
   - Check CPU usage
3. **Use shorter recordings**: Shorter audio processes faster
4. **Run locally instead of Replit**: Significant performance improvement

---

### ❌ Long delay between recording and translation

**Cause**: API processing time and network latency.

**Normal delays**:
- Speech recognition: 1-3 seconds
- Translation: 0.5-2 seconds
- Audio generation: 1-3 seconds
- **Total**: 3-8 seconds is normal

---

## Replit-Specific Issues

### ❌ "pip: ModuleNotFoundError" on Replit

**Solution**:
1. Refresh the Replit page
2. Stop the current process (Ctrl+C)
3. Clear pip cache:
   ```bash
   pip cache purge
   ```
4. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### ❌ Microphone not working on Replit

**Solution**:
1. Check browser microphone permissions:
   - Click 🔒 lock icon in address bar
   - Set Microphone to "Allow"
2. Refresh the Replit webview (Ctrl+R)
3. Try in a different browser
4. Ensure Replit gives audio permission

---

### ❌ "Connection refused" or "Port already in use"

**Solution**:
1. Stop the current Streamlit process
2. Wait 10 seconds
3. Run again: `streamlit run app.py`
4. Or specify a different port:
   ```bash
   streamlit run app.py --server.port 8502
   ```

---

### ❌ Large file size error after recording

**Solution**:
1. Keep recordings under 1 minute
2. Streamlit has a 200MB upload limit
3. Audio files are typically small (< 1MB)
4. If issue persists, check system storage space

---

## General FAQ

### Q: Why does the app ask for microphone permission?
**A**: The app needs microphone access to record your voice for translation. This is a browser security feature.

---

### Q: Is my audio data stored anywhere?
**A**: No. The app sends audio to Google Speech Recognition API, which processes and discards it. The app doesn't permanently store any audio.

---

### Q: What languages can I translate to?
**A**: Currently supports: Telugu, Hindi, French, Spanish, German, Marathi, Tamil, and Kannada. You can add more by editing the `LANGUAGE_MAP` in `app.py`.

---

### Q: Why does translation sometimes seem inaccurate?
**A**: Machine translation has limitations. Complex sentences, idioms, or technical terms may not translate perfectly. Breaking messages into simpler parts can help.

---

### Q: Can I use this offline?
**A**: No. The app requires internet for speech recognition, translation, and audio generation. All these services are cloud-based.

---

### Q: How do I add more languages?
**A**: Edit `app.py` and update the `LANGUAGE_MAP`:
```python
LANGUAGE_MAP = {
    "Telugu": "te",
    "Hindi": "hi",
    "Portuguese": "pt",  # Add new language
    "Russian": "ru",     # Add new language
}
```

Find language codes at: [ISO 639-1 Codes](https://en.wikipedia.org/wiki/ISO_639-1)

---

### Q: Can I use different translation services?
**A**: Yes! Replace `googletrans` with alternatives like:
- Microsoft Translator
- AWS Translate
- IBM Watson Language Translator

Modify the `translate_text()` function in `app.py` accordingly.

---

### Q: How do I improve speech recognition accuracy?
**A**: 
1. Use a good quality microphone
2. Speak clearly and at normal pace
3. Minimize background noise
4. Use standard English pronunciation
5. Break messages into shorter sentences

---

### Q: Can I run multiple instances?
**A**: Yes, on different ports:
```bash
streamlit run app.py --server.port 8501
streamlit run app.py --server.port 8502  # In another terminal
```

---

### Q: Is there a way to save translations?
**A**: Currently the app displays translations in the session. To save:
1. Screenshot the results
2. Copy-paste to a text file
3. Or modify the app to save to a database (advanced)

---

### Q: What's the maximum duration I can record?
**A**: The app allows up to 10 seconds per recording (configurable). This balance between:
- Allowing enough time to speak
- API rate limits
- Processing speed

You can adjust this in `app.py` near line 130.

---

### Q: Why does it say "Listening..." for a while?
**A**: This is the ambient noise adjustment period (1 second). Necessary for accurate speech detection. This is normal and expected.

---

## Still Having Issues?

1. **Check the error message**: It usually indicates the exact problem
2. **Review this guide**: Search for your specific error
3. **Check logs**: Look at terminal output for detailed error information
4. **Try from scratch**: Create a new virtual environment
5. **Update packages**: `pip install --upgrade -r requirements.txt`
6. **Restart system**: Sometimes helps with microphone issues

---

## Report Bugs

If you find a bug or issue not covered here:
1. Note the exact error message
2. Record the steps to reproduce
3. Include your system info (OS, Python version)
4. Check GitHub issues or create a new one

---

**Happy Translating! 🌍✨**

For more help, visit:
- [Streamlit Docs](https://docs.streamlit.io)
- [SpeechRecognition Docs](https://github.com/Uberi/speech_recognition)
- [Googletrans Docs](https://github.com/ssut/py-googletrans)
- [gTTS Docs](https://gtts.readthedocs.io)
