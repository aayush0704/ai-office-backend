from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "tiiuae/falcon-7b-instruct"  # Free & open-source model

print("Loading Falcon-7B model... (This may take time)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, 
    torch_dtype=torch.float32,  # Use CPU instead of GPU
    device_map="cpu"  # Ensures it runs on CPU (compatible with Render Free Tier)
)

def generate_ai_response(user_input):
    """Generates AI response using Falcon-7B"""
    inputs = tokenizer(user_input, return_tensors="pt").to("cpu")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
