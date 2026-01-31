#!/usr/bin/env python3
"""
SpyNet API Handler Examples

This file demonstrates how to use the API handlers programmatically
without the GUI. Useful for testing, automation, or integration.
"""

import json
import os
from api_handler import GeminiHandler, ChatGPTHandler


def load_config():
    """Load configuration from config.json"""
    config_path = "config.json"
    if not os.path.exists(config_path):
        config_path = "config.json.example"
    
    with open(config_path, 'r') as f:
        return json.load(f)


def example_gemini():
    """Example: Using Gemini API directly"""
    print("\n" + "="*50)
    print("Gemini API Example")
    print("="*50)
    
    config = load_config()
    handler = GeminiHandler(config.get("gemini_api_key", ""))
    
    prompt = "Explain what a desktop AI assistant is in one sentence."
    print(f"Query: {prompt}")
    print("\nResponse:")
    
    response = handler.query(prompt)
    print(response)


def example_chatgpt():
    """Example: Using ChatGPT API directly"""
    print("\n" + "="*50)
    print("ChatGPT API Example")
    print("="*50)
    
    config = load_config()
    handler = ChatGPTHandler(config.get("openai_api_key", ""))
    
    prompt = "What are the benefits of a stealth AI assistant?"
    print(f"Query: {prompt}")
    print("\nResponse:")
    
    response = handler.query(prompt)
    print(response)


def example_comparison():
    """Example: Compare responses from both APIs"""
    print("\n" + "="*50)
    print("API Comparison Example")
    print("="*50)
    
    config = load_config()
    gemini = GeminiHandler(config.get("gemini_api_key", ""))
    chatgpt = ChatGPTHandler(config.get("openai_api_key", ""))
    
    prompt = "What is Python?"
    print(f"Query: {prompt}\n")
    
    print("--- Gemini Response ---")
    gemini_response = gemini.query(prompt)
    print(gemini_response)
    
    print("\n--- ChatGPT Response ---")
    chatgpt_response = chatgpt.query(prompt)
    print(chatgpt_response)


def example_batch_queries():
    """Example: Process multiple queries"""
    print("\n" + "="*50)
    print("Batch Queries Example")
    print("="*50)
    
    config = load_config()
    handler = GeminiHandler(config.get("gemini_api_key", ""))
    
    queries = [
        "What is AI?",
        "What is machine learning?",
        "What is natural language processing?"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n{i}. Query: {query}")
        response = handler.query(query)
        print(f"   Response: {response[:100]}...")  # Show first 100 chars


def example_error_handling():
    """Example: Demonstrate error handling"""
    print("\n" + "="*50)
    print("Error Handling Example")
    print("="*50)
    
    # Try with empty API key
    handler = GeminiHandler("")
    
    print("Testing with empty API key:")
    response = handler.query("Hello")
    print(f"Response: {response}")
    
    print("\nThis demonstrates graceful error handling")
    print("The application continues to work in demo mode")


def main():
    """Run all examples"""
    print("SpyNet API Handler Examples")
    print("==========================")
    print("\nThese examples show how to use SpyNet's API handlers")
    print("programmatically without the GUI.\n")
    
    # Check if config exists
    if not os.path.exists("config.json"):
        print("Note: Using config.json.example (demo mode)")
        print("To test with real APIs, create config.json with your keys\n")
    
    # Run examples
    examples = [
        ("Error Handling (Demo Mode)", example_error_handling),
        # Uncomment these when you have API keys configured
        # ("Gemini API", example_gemini),
        # ("ChatGPT API", example_chatgpt),
        # ("API Comparison", example_comparison),
        # ("Batch Queries", example_batch_queries),
    ]
    
    for name, func in examples:
        try:
            func()
        except Exception as e:
            print(f"\nError in {name}: {e}")
    
    print("\n" + "="*50)
    print("Examples Complete")
    print("="*50)
    print("\nTo enable more examples:")
    print("1. Add your API keys to config.json")
    print("2. Uncomment the example functions in main()")
    print("3. Run this script again")


if __name__ == "__main__":
    main()
