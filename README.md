# SpyNet - Stealth AI Assistant 🕵️

A background desktop AI assistant that can be instantly shown or hidden using a toggle key, enabling discreet and fast access without interrupting workflow.

## Features

✨ **Quick Access** - Toggle visibility with a single hotkey (Ctrl+Shift+S)  
🤖 **Dual AI Integration** - Switch between ChatGPT and Gemini APIs  
🖥️ **Browser-Free Interface** - Standalone pop-up window for seamless usage  
🎨 **Optimized UI** - Clean, minimal interface with transparency and always-on-top  
⚡ **High Performance** - Lightweight background process with threaded query processing  
🔒 **Stealth Mode** - Hidden workflow that doesn't interrupt your tasks  

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Suraj-Singh-CSE/SpyNet.git
   cd SpyNet
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   
   Copy the example configuration file:
   ```bash
   cp config.json.example config.json
   ```
   
   Edit `config.json` and add your API keys:
   ```json
   {
       "gemini_api_key": "YOUR_GEMINI_API_KEY_HERE",
       "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",
       "toggle_key": "<ctrl>+<shift>+s"
   }
   ```

4. **Get API Keys**
   
   - **Gemini API**: Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **OpenAI API**: Get your key from [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

### Starting SpyNet

Run the application:
```bash
python spynet.py
```

The application will start in the background. You won't see any window initially.

### Using the Assistant

1. **Show/Hide** - Press `Ctrl+Shift+S` to toggle the assistant window
2. **Select AI Model** - Choose between Gemini or ChatGPT from the dropdown
3. **Enter Query** - Type your question in the input area
4. **Send** - Click "Send Query" or press `Ctrl+Enter`
5. **View Response** - AI-generated response appears in the response area
6. **Hide** - Press `Ctrl+Shift+S` again or click "Hide" to return to stealth mode

### Demo Mode

SpyNet works in demo mode even without API keys, providing simulated responses. This is useful for testing the interface and workflow before configuring APIs.

## Architecture

```
SpyNet/
├── spynet.py          # Main application with UI and keyboard handling
├── api_handler.py     # Gemini and ChatGPT API integration
├── config.json        # Configuration file (not tracked in git)
├── config.json.example # Example configuration template
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Key Components

### spynet.py
- Main application class (`SpyNetApp`)
- Tkinter-based UI with optimized layout
- Global keyboard listener for toggle functionality
- Threaded query processing for responsiveness
- Configuration management

### api_handler.py
- `GeminiHandler` - Google Gemini API integration
- `ChatGPTHandler` - OpenAI ChatGPT API integration
- Error handling and fallback mechanisms

## UI Optimization Features

- **Always on Top** - Window stays above other applications when visible
- **Transparency** - Slight alpha transparency (95%) for modern look
- **Clean Layout** - Organized sections for response and input
- **Keyboard Shortcuts** - Quick access with hotkeys
- **Status Bar** - Real-time feedback on application state
- **Responsive Design** - Smooth transitions and thread-based processing

## Performance Features

- **Background Process** - Minimal resource usage when hidden
- **Threaded API Calls** - Non-blocking query processing
- **Lazy Loading** - API handlers initialized only when needed
- **Efficient UI Updates** - Smart widget state management

## Troubleshooting

### Import Errors
If you see import errors, ensure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

### API Errors
- Verify your API keys are correct in `config.json`
- Check your internet connection
- Ensure your API keys have sufficient quota

### Keyboard Shortcut Not Working
- Try running with administrator/sudo privileges
- Check if another application is using the same hotkey
- Modify the `toggle_key` in `config.json` if needed

## Development Status

🚧 **Current Phase**: UI Optimization and System Performance Enhancement

### Completed
- ✅ Core application structure
- ✅ Keyboard toggle functionality
- ✅ Gemini API integration
- ✅ ChatGPT API integration
- ✅ Pop-up UI interface
- ✅ Configuration management
- ✅ Demo mode for testing

### In Progress
- 🔄 UI optimization (transparency, layout refinements)
- 🔄 Performance tuning (startup time, memory usage)
- 🔄 Enhanced error handling

### Planned
- 📋 Conversation history
- 📋 Custom themes
- 📋 More AI model options
- 📋 Voice input support
- 📋 Cross-platform optimization

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available for personal and educational use.

## Author

Developed by Suraj Singh

---

**Note**: This is an active development project. Features and functionality are continuously being improved.
