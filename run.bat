@echo off
REM ============================================================================
REM Run Script for Voice Translator - Windows Batch File
REM ============================================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/Update dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

REM Run Streamlit app
echo.
echo Starting Voice Translator app...
echo The app will open in your browser at: http://localhost:8501
echo.
streamlit run app.py

REM Keep console window open if there's an error
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to close this window.
    pause
)
