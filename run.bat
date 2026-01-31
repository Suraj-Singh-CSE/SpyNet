@echo off
REM SpyNet Launcher Script for Windows

echo Starting SpyNet - Stealth AI Assistant...
echo ==========================================
echo.

REM Check if config.json exists
if not exist "config.json" (
    echo Warning: config.json not found
    echo Creating config.json from example...
    copy config.json.example config.json
    echo Created config.json
    echo.
    echo Please edit config.json and add your API keys:
    echo   - Gemini API: https://makersuite.google.com/app/apikey
    echo   - OpenAI API: https://platform.openai.com/api-keys
    echo.
)

echo Starting SpyNet in background mode...
echo Press Ctrl+Shift+S to show/hide the assistant
echo.

REM Run SpyNet
python spynet.py
