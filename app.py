"""
Real-Time Voice Translation Web Application
A Streamlit-based application that translates speech from one language to another
with real-time microphone input, speech recognition, translation, and TTS output.
"""

import streamlit as st
import speech_recognition as sr
import os
from googletrans import Translator
from gtts import gTTS
import io
from datetime import datetime
import tempfile
st.set_page_config(
    page_title="VoiceAI",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Headings */
h1, h2, h3, h4 {
    color: #ffffff !important;
}

/* Force all text white */
p, span, label, div {
    color: #ffffff !important;
}

small {
    color: #cbd5e1 !important;
}

[data-testid="stMarkdownContainer"] {
    color: #ffffff !important;
}

.card * {
    color: #ffffff !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: white !important;
}
            /* Sidebar background */
section[data-testid="stSidebar"] {
    background: #0f172a !important;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* Sidebar headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

/* Sidebar divider */
section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.2) !important;
}

</style>
""", unsafe_allow_html=True)
# Language Map
LANGUAGE_MAP = {
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# Initialize session state
if "original_text" not in st.session_state:
    st.session_state.original_text = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""





# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================
if "original_text" not in st.session_state:
    st.session_state.original_text = ""
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Telugu"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def recognize_speech_from_microphone():
    """
    Capture audio from the microphone and convert it to text using Google Speech Recognition.
    
    Returns:
        tuple: (success: bool, text: str, error_message: str)
    """
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()
        
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            st.info("🎤 Listening... Please speak now!")
            
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Record audio with timeout
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        
        st.info("🔄 Processing your speech...")
        
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        return True, text, None
        
    except sr.UnknownValueError:
        error_msg = "❌ Could not understand audio. Please speak clearly and try again."
        return False, "", error_msg
    except sr.RequestError as e:
        error_msg = f"❌ Error accessing Google Speech Recognition service: {str(e)}"
        return False, "", error_msg
    except OSError:
        error_msg = "❌ Microphone not found. Please check your audio device."
        return False, "", error_msg
    except Exception as e:
        error_msg = f"❌ Unexpected error during recording: {str(e)}"
        return False, "", error_msg


def translate_text(text, target_language_code):
    """
    Translate text to the target language using Google Translate.
    
    Args:
        text (str): The text to translate
        target_language_code (str): The target language code (e.g., 'te', 'hi', 'fr')
    
    Returns:
        tuple: (success: bool, translated_text: str, error_message: str)
    """
    try:
        translator = Translator()
        result = translator.translate(text, src="en", dest=target_language_code)
        translated_text = result.text
        return True, translated_text, None

    except Exception as e:
        error_msg = f"❌ Translation failed: {str(e)}"
        return False, "", error_msg


def convert_text_to_speech(text, language_code):
    """
    Convert text to speech using Google Text-to-Speech (gTTS).
    
    Args:
        text (str): The text to convert to speech
        language_code (str): The language code for TTS
    
    Returns:
        tuple: (success: bool, audio_bytes: bytes, error_message: str)
    """
    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language_code, slow=False)
        
        # Save to BytesIO object instead of file
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        return True, audio_buffer.getvalue(), None
    except Exception as e:
        error_msg = f"❌ Text-to-Speech conversion failed: {str(e)}"
        return False, None, error_msg


# ============================================================================
# MAIN UI
# ============================================================================

# Header
st.title("🌍 Real-Time Voice Translator")
st.markdown("---")
st.markdown("**Translate your voice to any language in real-time!**")

# Sidebar for instructions
with st.sidebar:

    st.markdown("## 📖 How to Use")

    st.markdown("""
1. Select your target language  
2. Click **🎙 Start Recording**  
3. Speak clearly into your microphone  
4. Wait for the translation  
5. Listen to the translated audio
    """)

    st.markdown("---")

    st.markdown("## 🌍 Supported Languages")

    st.markdown("""
- Hindi  
- Telugu  
- Tamil  
- French  
- German  
- Spanish
    """)

# Language Selection
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("🗣️ Target Language")
    selected_language = st.selectbox(
        "Select Language:",
        list(LANGUAGE_MAP.keys()),
        index=0,
        label_visibility="collapsed"
    )
    st.session_state.selected_language = selected_language

# Recording Button
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎤 Start Recording", use_container_width=True, type="primary"):
        with st.spinner("Recording..."):
            # Step 1: Record and recognize speech
            success_recognize, original_text, error_recognize = recognize_speech_from_microphone()
            
            if success_recognize:
                st.session_state.original_text = original_text
                st.success("✅ Speech recognized successfully!")
                
                # Step 2: Translate the recognized text
                target_lang_code = LANGUAGE_MAP[selected_language]
                success_translate, translated_text, error_translate = translate_text(
                    original_text, 
                    target_lang_code
                )
                
                if success_translate:
                    st.session_state.translated_text = translated_text
                    st.success("✅ Translation completed!")
                    
                    # Step 3: Convert translated text to speech
                    success_tts, audio_bytes, error_tts = convert_text_to_speech(
                        translated_text, 
                        target_lang_code
                    )
                    
                    if success_tts:
                        st.success("✅ Audio generated successfully!")
                    else:
                        st.error(error_tts)
                else:
                    st.error(error_translate)
            else:
                st.error(error_recognize)

# Display Results
st.markdown("---")
st.subheader("📝 Results")

# Original Text Display
st.markdown("**Original Text (English):**", help="This is the speech you provided")

with st.container():
    original = st.session_state.get("original_text", "")
    if original:
        st.write(original)
    else:
        st.write("*No speech recorded yet*")

# Translated Text Display
st.markdown(f"**Translated Text ({selected_language}):**", help="This is the translated version of your speech")
translated_container = st.container()
with st.container():
    if st.session_state.translated_text:
        st.write(st.session_state.translated_text)
    else:
        st.write("*Translation will appear here*")

# Audio Playback
if st.session_state.translated_text:
    st.markdown("---")
    st.subheader("🔊 Listen to Translation")
    
    # Generate audio for playback
    success_tts, audio_bytes, error_tts = convert_text_to_speech(
        st.session_state.translated_text,
        LANGUAGE_MAP[selected_language]
    )
    
    if success_tts and audio_bytes:
        st.audio(audio_bytes, format="audio/mp3")
        st.markdown("*Click the player above to listen to the translated text*")
    else:
        st.warning("Could not generate audio for playback")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
    🌐 Real-Time Voice Translation App | Built with Streamlit
    </div>
    """, unsafe_allow_html=True)
