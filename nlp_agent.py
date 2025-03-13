import os
import requests
import json

# OpenRouter API Details for DeepSeek
API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Fetch from Render Environment Variables
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def generate_ai_response(user_input):
    """Generates AI response using DeepSeek via OpenRouter API"""
    if not OPENROUTER_API_KEY:
        return "Error: Missing OpenRouter API key."

    payload = {
        "model": "deepseek/deepseek-r1:free",  # Free-tier DeepSeek model
        "messages": [{"role": "user", "content": user_input}]
    }
    
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise error for HTTP issues

        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return "Error: Unexpected response format from DeepSeek API."

    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to DeepSeek API - {e}"
