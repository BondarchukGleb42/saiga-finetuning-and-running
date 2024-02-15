from fastapi import FastAPI
from llama_cpp import Llama
import os

app = FastAPI()

PATH = os.path.dirname(os.path.abspath(__file__))
MODEL_NAME = "model.gguf"
model = Llama(model_path=os.path.join(PATH, MODEL_NAME), n_gpu_layers=128, n_ctx=2048)

SYSTEM_PROMPT = "any system prompt"



@app.post("/chat")
def get_predict(question: str):
    prompt = f"""<s>system{SYSTEM_PROMPT}</s><s>user{question}</s><s>bot"""
    output = model(
        prompt,
        max_tokens=2048,
        echo=False,
        temperature=1,
    )

    return {"predict": output["choices"][0]["text"]}
