from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

print("Loading LLaMA 2 model... (This may take time)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32, device_map="cpu")  # Use CPU instead of GPU

def generate_ai_response(user_input):
    """Generates AI response using LLaMA 2"""
    inputs = tokenizer(user_input, return_tensors="pt").to("cpu")  # Change to CPU
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
