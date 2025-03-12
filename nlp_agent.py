from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "openchat/openchat-3.5"

print("Loading OpenChat-3.5 model... (This may take time)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32, device_map="cpu")

def generate_ai_response(user_input):
    """Generates AI response using OpenChat-3.5"""
    inputs = tokenizer(user_input, return_tensors="pt").to("cpu")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
