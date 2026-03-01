#!/bin/bash

# ============================================================================
# Run Script for Voice Translator - Bash Script for Unix/Linux/macOS
# ============================================================================

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Please install Python 3.8 or higher from https://www.python.org/"
    exit 1
fi

# Show Python version
echo -e "${GREEN}Found Python:$(python3 --version)${NC}"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${GREEN}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Install/Update dependencies
echo -e "${GREEN}Installing dependencies...${NC}"
pip install -r requirements.txt --quiet

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to install dependencies${NC}"
    exit 1
fi

# Run Streamlit app
echo -e "${GREEN}Starting Voice Translator app...${NC}"
echo "The app will open in your browser at: http://localhost:8501"
echo ""

streamlit run app.py

# Check if Streamlit exited with an error
if [ $? -ne 0 ]; then
    echo -e "${RED}An error occurred while running the app${NC}"
    exit 1
fi
