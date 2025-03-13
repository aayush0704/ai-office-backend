import os
import requests

# Hugging Face API Details
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")  # Fetch from Render Environment Variables
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_ai_response(user_input):
    """Generates AI response using Hugging Face API (Falcon-7B)"""
    if not HUGGINGFACE_API_TOKEN:
        return "Error: Missing Hugging Face API token."

    payload = {"inputs": user_input}
    
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise error for HTTP issues

        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "Error: Unexpected response format from Hugging Face API."

    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to Hugging Face API - {e}"
