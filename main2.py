from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

class MedicalTextRequest(BaseModel):
    text: str

class MedicalTextResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=MedicalTextResponse)
async def summarize_medical_text(request: MedicalTextRequest):
    try:
        summary = summarizer(request.text, max_length=2000, min_length=1500, do_sample=False)[0]['summary_text']
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}