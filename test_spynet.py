#!/usr/bin/env python3
"""
Test script for SpyNet components
Tests core functionality without requiring GUI or API keys
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    try:
        import api_handler
        print("✓ api_handler module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import api_handler: {e}")
        return False
    
    return True

def test_api_handlers():
    """Test API handler initialization"""
    print("\nTesting API handlers...")
    from api_handler import GeminiHandler, ChatGPTHandler
    
    # Test without API keys (should handle gracefully)
    gemini = GeminiHandler("")
    chatgpt = ChatGPTHandler("")
    
    print("✓ GeminiHandler initialized")
    print("✓ ChatGPTHandler initialized")
    
    # Test demo queries
    print("\nTesting demo query responses...")
    gemini_response = gemini.query("Hello")
    chatgpt_response = chatgpt.query("Hello")
    
    if "Error" in gemini_response and "not configured" in gemini_response:
        print("✓ Gemini correctly reports missing API key")
    
    if "Error" in chatgpt_response and "not configured" in chatgpt_response:
        print("✓ ChatGPT correctly reports missing API key")
    
    return True

def test_config():
    """Test configuration file"""
    print("\nTesting configuration...")
    import json
    
    config_example = "config.json.example"
    if os.path.exists(config_example):
        with open(config_example, 'r') as f:
            config = json.load(f)
        
        required_keys = ["gemini_api_key", "openai_api_key", "toggle_key"]
        for key in required_keys:
            if key in config:
                print(f"✓ Config has '{key}'")
            else:
                print(f"✗ Config missing '{key}'")
                return False
    else:
        print(f"✗ {config_example} not found")
        return False
    
    return True

def test_requirements():
    """Test requirements file exists"""
    print("\nTesting requirements.txt...")
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", 'r') as f:
            content = f.read()
        
        required_packages = ["pynput", "google-generativeai", "openai"]
        for pkg in required_packages:
            if pkg in content:
                print(f"✓ Requirements includes '{pkg}'")
            else:
                print(f"✗ Requirements missing '{pkg}'")
    else:
        print("✗ requirements.txt not found")
        return False
    
    return True

def main():
    """Run all tests"""
    print("=" * 50)
    print("SpyNet Component Tests")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_api_handlers,
        test_config,
        test_requirements
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"\n✗ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 50)
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
