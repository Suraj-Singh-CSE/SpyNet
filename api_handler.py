"""
API Handlers for Gemini and ChatGPT integration
"""

import os


class GeminiHandler:
    """Handler for Google Gemini API"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = None
        
        if api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-pro')
            except ImportError:
                print("Warning: google-generativeai not installed. Install it with: pip install google-generativeai")
            except Exception as e:
                print(f"Error initializing Gemini: {e}")
    
    def query(self, prompt):
        """Send query to Gemini and get response"""
        if not self.model:
            return "Error: Gemini API not configured. Please add your API key to config.json"
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error querying Gemini: {str(e)}"


class ChatGPTHandler:
    """Handler for OpenAI ChatGPT API"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = None
        
        if api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=api_key)
            except ImportError:
                print("Warning: openai not installed. Install it with: pip install openai")
            except Exception as e:
                print(f"Error initializing ChatGPT: {e}")
    
    def query(self, prompt):
        """Send query to ChatGPT and get response"""
        if not self.client:
            return "Error: ChatGPT API not configured. Please add your API key to config.json"
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error querying ChatGPT: {str(e)}"
