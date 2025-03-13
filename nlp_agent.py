import os
import requests
import json

# OpenRouter API Details for DeepSeek
API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("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")  # Fetch from Render Environment Variables
HEADERS = {
    "Authorization": f"Bearer {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}",
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
