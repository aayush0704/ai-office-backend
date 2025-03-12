from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

print("Loading LLaMA 2 model... (This may take some time)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, 
    torch_dtype=torch.float32,  # Use float32 for CPU compatibility
    device_map="cpu"  # Ensure it runs on CPU
)

def generate_ai_response(user_input):
    """Generates AI response using LLaMA 2"""
    inputs = tokenizer(user_input, return_tensors="pt").to("cpu")  # Move model to CPU
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
