# 🌍 Real-Time Voice Translation Web Application

A modern web application built with **Streamlit** that translates your voice in real-time to multiple languages with automatic speech-to-text, translation, and text-to-speech synthesis.

## 🌟 Features

- **Real-time Microphone Recording**: Capture audio directly from your device
- **Speech-to-Text**: Convert voice to text using Google Speech Recognition
- **Multi-language Translation**: Translate to Telugu, Hindi, French, Spanish, German, Marathi, Tamil, and Kannada
- **Text-to-Speech**: Hear the translated text in the target language
- **Auto Audio Playback**: Play translated audio automatically
- **Error Handling**: Comprehensive error messages for microphone and connectivity issues
- **Clean UI**: User-friendly interface with dark mode support
- **Session Management**: Keep track of translations during your session

## 📋 Prerequisites

- Python 3.8 or higher
- Microphone access
- Internet connection (for translation and speech synthesis)
- pip (Python package manager)

## 🚀 Installation & Setup

### Local Machine Setup

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd multilingual-translator
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Access the App**
   - The app will automatically open in your default browser
   - Usually available at: `http://localhost:8501`

### Replit Setup

1. **Create a New Replit Project**
   - Go to [Replit.com](https://replit.com)
   - Click "Create" → Select "Python"
   - Name your project

2. **Upload Files**
   - Upload `app.py` and `requirements.txt` to your Replit project

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Access via Replit's Webview**
   - Replit will show a webview panel where the app runs
   - Click "Open in new tab" to open in a full browser window

## 📁 Project Structure

```
multilingual-translator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## 🎯 How to Use

1. **Select Target Language**: Choose from the dropdown menu (Telugu, Hindi, French, Spanish, etc.)
2. **Click "Start Recording"**: Press the blue recording button
3. **Speak Clearly**: Speak your message into the microphone
4. **Wait for Processing**: The app will:
   - Recognize your speech
   - Translate to the selected language
   - Generate audio for the translation
5. **Listen to Translation**: Use the audio player to hear the translated text

## 🔧 Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web UI framework |
| `SpeechRecognition` | Speech-to-text using Google API |
| `googletrans` | Text translation service |
| `gTTS` | Google Text-to-Speech |
| `pyaudio` | Microphone access and audio I/O |

## 🌐 Supported Languages

- 🇮🇳 Telugu
- 🇮🇳 Hindi
- 🇫🇷 French
- 🇪🇸 Spanish
- 🇩🇪 German
- 🇮🇳 Marathi
- 🇮🇳 Tamil
- 🇮🇳 Kannada

You can easily add more languages by updating the `LANGUAGE_MAP` dictionary in `app.py`.

## ⚠️ Troubleshooting

### Microphone Not Detected
- **Windows**: Check audio settings and ensure the app has microphone permissions
- **Replit**: Use the Replit audio input feature in the webview
- **Solution**: Run `python -m speech_recognition` to diagnose issues

### Speech Not Recognized
- Speak clearly and at a steady pace
- Reduce background noise
- Ensure proper microphone positioning
- Wait a few seconds after the "Listening..." prompt

### Translation Not Working
- Check your internet connection
- Try again after a few seconds
- Alternative: Use a different language pair

### Audio Playback Issues
- Ensure your speakers/headphones are working
- Check volume levels
- Try the browser's default audio player

### ImportError for `pyaudio` on Replit
- Replit handles audio input through its webview
- If using locally on Linux, install: `sudo apt-get install portaudio19-dev`
- On macOS: `brew install portaudio`

## 📝 Code Comments

The code is fully commented with explanations for:
- Session state management
- Speech recognition configuration
- Translation API usage
- Text-to-speech generation
- Error handling strategies
- UI component layout

## 🔐 Privacy & Security

- All audio processing happens through Google APIs
- No audio is permanently stored
- Translations are not logged
- Your microphone input is transmitted only for processing

## 📚 API Documentation References

- [SpeechRecognition Library](https://github.com/Uberi/speech_recognition)
- [Googletrans](https://github.com/ssut/py-googletrans)
- [gTTS](https://gtts.readthedocs.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🐛 Reporting Issues

If you encounter any bugs or issues:
1. Check the troubleshooting section
2. Review the error message displayed
3. Ensure all dependencies are correctly installed
4. Try running in a fresh virtual environment

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork, modify, and enhance this project. Some ideas for improvement:
- Add support for more languages
- Implement audio file upload
- Add translation history
- Support for batch translations
- Custom voice preferences

## 💡 Tips for Best Results

1. **Clear Audio**: Speak in a quiet environment for better recognition
2. **Natural Pace**: Speak at your normal conversational pace
3. **Short Sentences**: Break your message into shorter phrases for better accuracy
4. **Test Microphone**: Test your microphone in system settings before using the app
5. **Internet Connection**: Ensure a stable internet connection for translation and TTS

---

**Enjoy translating! 🌍✨**

Made with ❤️ using Streamlit
"# MULTILINGUAL-TRANSLATOR" 
"# MULTILINGUAL-TRANSLATOR" 
