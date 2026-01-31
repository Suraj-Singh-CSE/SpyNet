#!/usr/bin/env python3
"""
SpyNet - Stealth AI Assistant
A background desktop AI assistant with quick toggle access
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import sys
from pynput import keyboard
import json
import os

# Import API handlers
try:
    from api_handler import GeminiHandler, ChatGPTHandler
except ImportError:
    # Fallback if API handlers not available
    GeminiHandler = None
    ChatGPTHandler = None


class SpyNetApp:
    """Main SpyNet application class"""
    
    def __init__(self):
        self.root = None
        self.visible = False
        self.current_api = "gemini"
        self.config = self.load_config()
        
        # Initialize API handlers
        self.gemini_handler = None
        self.chatgpt_handler = None
        
        if GeminiHandler:
            self.gemini_handler = GeminiHandler(self.config.get("gemini_api_key", ""))
        if ChatGPTHandler:
            self.chatgpt_handler = ChatGPTHandler(self.config.get("openai_api_key", ""))
        
        # Create the UI
        self.create_ui()
        
        # Setup keyboard listener
        self.setup_keyboard_listener()
    
    def load_config(self):
        """Load configuration from config.json"""
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
        return {
            "gemini_api_key": "",
            "openai_api_key": "",
            "toggle_key": "<ctrl>+<shift>+s"
        }
    
    def create_ui(self):
        """Create the main UI window"""
        self.root = tk.Tk()
        self.root.title("SpyNet - AI Assistant")
        self.root.geometry("600x500")
        
        # Make window stay on top and frameless for stealth look
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.95)  # Slight transparency
        
        # Configure grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Top frame with controls
        top_frame = ttk.Frame(self.root, padding="5")
        top_frame.grid(row=0, column=0, sticky="ew")
        
        # API selector
        ttk.Label(top_frame, text="AI Model:").pack(side=tk.LEFT, padx=5)
        self.api_var = tk.StringVar(value="gemini")
        api_combo = ttk.Combobox(top_frame, textvariable=self.api_var, 
                                  values=["gemini", "chatgpt"], width=10, state="readonly")
        api_combo.pack(side=tk.LEFT, padx=5)
        api_combo.bind("<<ComboboxSelected>>", self.on_api_change)
        
        # Close button
        close_btn = ttk.Button(top_frame, text="Hide (Ctrl+Shift+S)", command=self.toggle_visibility)
        close_btn.pack(side=tk.RIGHT, padx=5)
        
        # Response area
        response_frame = ttk.LabelFrame(self.root, text="AI Response", padding="5")
        response_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        response_frame.grid_rowconfigure(0, weight=1)
        response_frame.grid_columnconfigure(0, weight=1)
        
        self.response_text = scrolledtext.ScrolledText(response_frame, wrap=tk.WORD, 
                                                        height=15, width=70)
        self.response_text.grid(row=0, column=0, sticky="nsew")
        self.response_text.config(state=tk.DISABLED)
        
        # Input area
        input_frame = ttk.LabelFrame(self.root, text="Your Query", padding="5")
        input_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        input_frame.grid_columnconfigure(0, weight=1)
        
        self.input_text = tk.Text(input_frame, wrap=tk.WORD, height=4)
        self.input_text.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=1, column=0, sticky="ew", padx=5)
        
        self.send_btn = ttk.Button(button_frame, text="Send Query", command=self.send_query)
        self.send_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_input)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready - Press Ctrl+Shift+S to toggle")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=3, column=0, sticky="ew")
        
        # Bind Enter key to send
        self.input_text.bind("<Control-Return>", lambda e: self.send_query())
        
        # Start hidden
        self.root.withdraw()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.toggle_visibility)
    
    def on_api_change(self, event=None):
        """Handle API selection change"""
        self.current_api = self.api_var.get()
        self.update_status(f"Switched to {self.current_api.upper()}")
    
    def clear_input(self):
        """Clear the input text"""
        self.input_text.delete("1.0", tk.END)
    
    def update_status(self, message):
        """Update status bar"""
        self.status_var.set(message)
    
    def append_response(self, text):
        """Append text to response area"""
        self.response_text.config(state=tk.NORMAL)
        self.response_text.insert(tk.END, text + "\n\n")
        self.response_text.see(tk.END)
        self.response_text.config(state=tk.DISABLED)
    
    def send_query(self):
        """Send query to selected AI API"""
        query = self.input_text.get("1.0", tk.END).strip()
        
        if not query:
            self.update_status("Please enter a query")
            return
        
        # Disable send button while processing
        self.send_btn.config(state=tk.DISABLED)
        self.update_status("Processing query...")
        
        # Clear previous response
        self.response_text.config(state=tk.NORMAL)
        self.response_text.delete("1.0", tk.END)
        self.response_text.config(state=tk.DISABLED)
        
        # Process in background thread
        thread = threading.Thread(target=self._process_query, args=(query,))
        thread.daemon = True
        thread.start()
    
    def _process_query(self, query):
        """Process query in background thread"""
        try:
            response = None
            
            if self.current_api == "gemini" and self.gemini_handler:
                response = self.gemini_handler.query(query)
            elif self.current_api == "chatgpt" and self.chatgpt_handler:
                response = self.chatgpt_handler.query(query)
            else:
                response = f"[Demo Mode] This is a simulated response to: {query}\n\n" \
                          f"To use real AI responses, please:\n" \
                          f"1. Add your API keys to config.json\n" \
                          f"2. Install required packages: pip install -r requirements.txt"
            
            # Update UI in main thread
            self.root.after(0, self._display_response, response)
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.root.after(0, self._display_response, error_msg)
    
    def _display_response(self, response):
        """Display response in UI (runs in main thread)"""
        self.append_response(response)
        self.send_btn.config(state=tk.NORMAL)
        self.update_status("Ready")
    
    def toggle_visibility(self):
        """Toggle window visibility"""
        if self.visible:
            self.root.withdraw()
            self.visible = False
        else:
            self.root.deiconify()
            self.root.lift()
            self.root.focus_force()
            self.input_text.focus()
            self.visible = True
    
    def setup_keyboard_listener(self):
        """Setup global keyboard listener for toggle key"""
        def on_activate():
            # Toggle visibility when hotkey pressed
            self.root.after(0, self.toggle_visibility)
        
        # Ctrl+Shift+S as toggle key
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<ctrl>+<shift>+s'),
            on_activate
        )
        
        def for_canonical(f):
            return lambda k: f(listener.canonical(k))
        
        listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)
        )
        
        listener.start()
    
    def run(self):
        """Start the application"""
        print("SpyNet is running in the background...")
        print("Press Ctrl+Shift+S to show/hide the assistant")
        self.root.mainloop()


def main():
    """Main entry point"""
    app = SpyNetApp()
    app.run()


if __name__ == "__main__":
    main()
