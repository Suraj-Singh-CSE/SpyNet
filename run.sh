#!/bin/bash
# SpyNet Launcher Script

echo "Starting SpyNet - Stealth AI Assistant..."
echo "=========================================="
echo ""

# Check if config.json exists
if [ ! -f "config.json" ]; then
    echo "⚠️  Warning: config.json not found"
    echo "Creating config.json from example..."
    cp config.json.example config.json
    echo "✓ Created config.json"
    echo ""
    echo "Please edit config.json and add your API keys:"
    echo "  - Gemini API: https://makersuite.google.com/app/apikey"
    echo "  - OpenAI API: https://platform.openai.com/api-keys"
    echo ""
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "Starting SpyNet in background mode..."
echo "Press Ctrl+Shift+S to show/hide the assistant"
echo ""

# Run SpyNet
python3 spynet.py
