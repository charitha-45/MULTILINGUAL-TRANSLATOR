"""
Configuration file for Replit environment
Contains environment-specific settings and optimizations
"""

import os

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

# Enable browser output for Replit
os.environ['STREAMLIT_CLIENT_TOOLBARPOSITION'] = 'bottom'
os.environ['STREAMLIT_LOGGER_LEVEL'] = 'info'

# Audio configuration for Replit
REPLIT_AUDIO_ENABLED = True

# Timeout settings (in seconds)
SPEECH_RECOGNITION_TIMEOUT = 10
SPEECH_RECOGNITION_PHRASE_LIMIT = 10

# API rate limiting
TRANSLATION_API_CALLS_PER_MINUTE = 60
TTS_API_CALLS_PER_MINUTE = 60

# Supported languages
SUPPORTED_LANGUAGES = {
    "Telugu": "te",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Marathi": "mr",
    "Tamil": "ta",
    "Kannada": "kn"
}

# UI Configuration
UI_CONFIG = {
    "page_title": "Voice Translator",
    "page_icon": "🌍",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOG_CONFIG = {
    'level': 'INFO',
    'format': '[%(asctime)s] %(levelname)s: %(message)s'
}

# ============================================================================
# ERROR MESSAGES
# ============================================================================

ERROR_MESSAGES = {
    'microphone_not_found': "❌ Microphone not found. Please check your audio device.",
    'audio_not_understood': "❌ Could not understand audio. Please speak clearly and try again.",
    'api_error': "❌ API error occurred. Please check your internet connection.",
    'translation_failed': "❌ Translation failed. Please try again.",
    'tts_failed': "❌ Text-to-Speech conversion failed.",
    'recording_timeout': "❌ Recording timeout. Please try again.",
    'unexpected_error': "❌ An unexpected error occurred."
}

# ============================================================================
# SUCCESS MESSAGES
# ============================================================================

SUCCESS_MESSAGES = {
    'recording_started': "🎤 Listening... Please speak now!",
    'speech_recognized': "✅ Speech recognized successfully!",
    'translation_complete': "✅ Translation completed!",
    'audio_generated': "✅ Audio generated successfully!",
    'processing': "🔄 Processing your speech..."
}
