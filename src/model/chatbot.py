from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from typing import List, Dict

class Chatbot:
    def __init__(self, model_name: str = 'gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_response(self, query: str, context: List[Dict[str, str]], max_length: int = 150) -> str:
        context_text = " ".join([doc['text'] for doc in context])
        prompt = f"Context: {context_text}\n\nQuestion: {query}\n\nAnswer:"
        
        inputs = self.tokenizer.encode(prompt, return_tensors='pt').to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                top_k=50,
                top_p=0.95,
                temperature=0.7
            )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        answer = generated_text.split("Answer:")[-1].strip()
        return answer