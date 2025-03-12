from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load LLaMA 2 model from Hugging Face
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"  # You can use a smaller model if needed

print("Loading LLaMA 2 model... (This may take time)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

def generate_ai_response(user_input):
    """Generates AI response using LLaMA 2"""
    inputs = tokenizer(user_input, return_tensors="pt").to("cuda")  # Use GPU if available
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=200)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
