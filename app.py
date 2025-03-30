from fastapi import FastAPI, HTTPException
from transformers import pipeline
from models import SummarizationRequest
import os
import dotenv

dotenv.load_dotenv()

app = FastAPI()

summarizer = pipeline("summarization", model=os.getenv("MODEL_ID"), device='mps')

@app.post("/summarize")
def summarize_text(request:SummarizationRequest):
    if len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    
    summary = summarizer(
        request.text, 
        max_length=request.max_length, 
        min_length=request.min_length,
        do_sample=True,
        temperature=0.1
    )
    
    return {"summary": summary[0]["summary_text"]}