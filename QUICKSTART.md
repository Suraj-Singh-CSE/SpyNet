# SpyNet Quick Start Guide

## 🚀 Getting Started in 3 Minutes

### Step 1: Install Dependencies

```bash
pip install pynput
```

**Note**: The full requirements.txt includes optional packages for API integration. If you just want to test the interface, `pynput` is sufficient to start.

### Step 2: Configure (Optional)

For demo mode (testing without API keys):
- Just run the application directly
- It will work with simulated responses

For full functionality with AI:
```bash
cp config.json.example config.json
# Edit config.json and add your API keys
```

### Step 3: Run

**Linux/Mac:**
```bash
python3 spynet.py
```

**Windows:**
```bash
python spynet.py
```

Or use the launcher scripts:
- Linux/Mac: `./run.sh`
- Windows: `run.bat`

### Step 4: Use

1. **Show Assistant**: Press `Ctrl+Shift+S`
2. **Type Query**: Enter your question
3. **Get Response**: Click "Send Query" or press `Ctrl+Enter`
4. **Hide Assistant**: Press `Ctrl+Shift+S` again

## 💡 Tips

- The application runs in the background, so you won't see a window initially
- Use `Ctrl+Shift+S` to toggle visibility at any time
- The window stays on top when visible for quick access
- In demo mode, you'll get simulated responses to test the interface

## 🔑 Getting API Keys (For Full Functionality)

### Gemini API (Free Tier Available)
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key to `config.json`

### OpenAI API (Paid Service)
1. Visit: https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key to `config.json`

## ⚠️ Troubleshooting

### "ModuleNotFoundError: No module named 'pynput'"
```bash
pip install pynput
```

### "ModuleNotFoundError: No module named 'tkinter'"
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **Fedora**: `sudo dnf install python3-tkinter`
- **macOS**: Included with Python
- **Windows**: Included with Python

### Keyboard shortcut not working
- Try running with administrator/sudo privileges
- Some systems require elevated permissions for global hotkeys

### API not responding
- Check internet connection
- Verify API key is correct in config.json
- Check API service status
- Ensure you have API quota remaining

## 📚 Next Steps

- Read the full README.md for detailed documentation
- Customize the toggle key in config.json
- Experiment with both Gemini and ChatGPT models
- Share feedback and contribute!

---

**Need Help?** Open an issue on GitHub or check the README.md for more details.
