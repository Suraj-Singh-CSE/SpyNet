# SpyNet Architecture

## Overview

SpyNet is a desktop AI assistant built with Python, featuring a stealth workflow and dual AI integration. This document describes the system architecture and design decisions.

## System Components

```
┌─────────────────────────────────────────────────────┐
│                   SpyNet Application                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌────────────────────────────────────────────┐   │
│  │         Keyboard Listener (pynput)         │   │
│  │     Global Hotkey: Ctrl+Shift+S            │   │
│  └──────────────────┬─────────────────────────┘   │
│                     │                              │
│                     ▼                              │
│  ┌────────────────────────────────────────────┐   │
│  │         SpyNetApp (Main Controller)        │   │
│  │  - UI Management                           │   │
│  │  - State Management (visible/hidden)       │   │
│  │  - Configuration Loading                   │   │
│  │  - API Routing                             │   │
│  └──────────────┬──────────────┬──────────────┘   │
│                 │              │                   │
│        ┌────────▼────┐    ┌────▼────────┐        │
│        │   UI Layer   │    │  API Layer  │        │
│        │   (tkinter)  │    │             │        │
│        └──────────────┘    └─────────────┘        │
│              │                    │                │
│              │                    │                │
│  ┌───────────▼──────────┐   ┌────▼──────────┐   │
│  │  Main Window         │   │ GeminiHandler  │   │
│  │  - Input Text Area   │   │ ChatGPTHandler │   │
│  │  - Response Display  │   └────────────────┘   │
│  │  - API Selector      │          │             │
│  │  - Status Bar        │          │             │
│  └──────────────────────┘          │             │
│                                     │             │
└─────────────────────────────────────┼─────────────┘
                                      │
                          ┌───────────▼───────────┐
                          │   External APIs       │
                          │  - Google Gemini      │
                          │  - OpenAI ChatGPT     │
                          └───────────────────────┘
```

## Core Modules

### 1. spynet.py (Main Application)

**Purpose**: Main application entry point and UI controller

**Key Classes**:
- `SpyNetApp`: Main application class

**Responsibilities**:
- Initialize UI components
- Manage application state (visible/hidden)
- Handle keyboard events
- Route queries to appropriate API handler
- Manage threading for async operations
- Load and apply configuration

**Key Methods**:
- `create_ui()`: Build the tkinter interface
- `setup_keyboard_listener()`: Configure global hotkey
- `toggle_visibility()`: Show/hide the application
- `send_query()`: Process user queries
- `_process_query()`: Background thread for API calls

### 2. api_handler.py (API Integration)

**Purpose**: Interface with external AI APIs

**Key Classes**:
- `GeminiHandler`: Google Gemini API integration
- `ChatGPTHandler`: OpenAI ChatGPT API integration

**Responsibilities**:
- Initialize API clients with keys
- Send queries to AI services
- Handle API errors gracefully
- Return formatted responses

**Key Methods**:
- `query(prompt)`: Send prompt to AI and return response

### 3. config.json (Configuration)

**Purpose**: Store user settings and API credentials

**Structure**:
```json
{
    "gemini_api_key": "API_KEY",
    "openai_api_key": "API_KEY",
    "toggle_key": "<ctrl>+<shift>+s"
}
```

## Design Patterns

### 1. Singleton Pattern (Implicit)
- Single SpyNetApp instance controls the entire application
- Ensures one UI window and one keyboard listener

### 2. Strategy Pattern
- API handlers are interchangeable
- User can switch between Gemini and ChatGPT at runtime

### 3. Observer Pattern
- Keyboard listener observes global keyboard events
- Triggers UI visibility changes

### 4. Threading Pattern
- API calls run in background threads
- Prevents UI freezing during network operations
- Uses `root.after()` for thread-safe UI updates

## Key Design Decisions

### Why Python + tkinter?

**Advantages**:
- Cross-platform compatibility
- No external browser required
- Lightweight and fast
- Native look and feel
- Easy distribution

**Trade-offs**:
- Limited styling compared to web frameworks
- Less modern UI capabilities

### Why pynput for Keyboard Handling?

**Advantages**:
- Cross-platform global hotkeys
- Reliable event handling
- Simple API

**Trade-offs**:
- May require elevated permissions on some systems
- Platform-specific quirks

### Threading Model

**Background Thread for API Calls**:
```python
thread = threading.Thread(target=self._process_query, args=(query,))
thread.daemon = True
thread.start()
```

**UI Updates in Main Thread**:
```python
self.root.after(0, self._display_response, response)
```

This ensures:
- Responsive UI during API calls
- Thread-safe tkinter operations
- Proper cleanup on exit

## Performance Optimizations

### 1. Lazy Loading
- API handlers only initialized if keys provided
- Modules imported only when needed

### 2. Efficient UI Updates
- Disabled text widgets during updates
- Batch UI operations
- Smart widget state management

### 3. Background Processing
- Network calls in separate threads
- Non-blocking query processing
- Daemon threads for automatic cleanup

### 4. Minimal Resource Usage
- Single window instance
- Efficient event handling
- No continuous polling

## Security Considerations

### API Key Storage
- Stored in local config.json
- Not committed to version control (.gitignore)
- Loaded at runtime only

### Input Validation
- Basic input sanitization
- Error handling for malformed queries
- Safe JSON parsing

### Network Security
- Uses official API client libraries
- HTTPS connections
- No custom network code

## Extensibility

### Adding New AI Models

1. Create new handler class in `api_handler.py`:
```python
class NewAIHandler:
    def __init__(self, api_key):
        # Initialize
        pass
    
    def query(self, prompt):
        # Process query
        return response
```

2. Initialize in `SpyNetApp.__init__()`:
```python
self.newai_handler = NewAIHandler(config.get("newai_key"))
```

3. Add to API selector in `create_ui()`:
```python
values=["gemini", "chatgpt", "newai"]
```

4. Update routing in `_process_query()`:
```python
elif self.current_api == "newai":
    response = self.newai_handler.query(query)
```

### Adding New Features

**Conversation History**:
- Add list to store query/response pairs
- Add UI elements for history display
- Implement save/load functionality

**Custom Themes**:
- Create theme configuration
- Add theme selector to UI
- Apply colors and fonts dynamically

## Testing Strategy

### Unit Tests
- Test API handlers independently
- Test configuration loading
- Test UI component creation

### Integration Tests
- Test end-to-end query flow
- Test keyboard shortcut handling
- Test API switching

### Manual Testing
- Cross-platform compatibility
- UI responsiveness
- Error handling

## Future Architecture Considerations

### Plugin System
- Define plugin interface
- Dynamic plugin loading
- Isolated plugin execution

### Local AI Support
- Integration with local LLMs (Ollama, LM Studio)
- Offline capability
- Privacy-focused option

### Cloud Sync
- Optional conversation history sync
- Cross-device configuration
- Encrypted storage

## Dependencies

### Core Dependencies
- **tkinter**: GUI framework (standard library)
- **pynput**: Keyboard monitoring
- **threading**: Async operations (standard library)
- **json**: Configuration (standard library)

### Optional Dependencies
- **google-generativeai**: Gemini API
- **openai**: ChatGPT API

### Development Dependencies
- **python**: 3.7+
- Standard library modules

## Performance Metrics

### Startup Time
- Target: < 1 second
- Current: ~0.5 seconds (without API initialization)

### Toggle Response
- Target: < 100ms
- Current: ~50ms (instant visibility toggle)

### Memory Usage
- Base: ~30-50 MB
- With API handlers: ~50-80 MB

### Network Latency
- Depends on API service
- Gemini: ~1-3 seconds
- ChatGPT: ~1-2 seconds

---

This architecture document will be updated as the system evolves.
