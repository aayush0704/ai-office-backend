import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_ai_response(user_input):
    """Generates an AI response using GPT-4"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
