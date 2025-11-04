from fastapi import FastAPI, UploadFile, File, Form
import asyncio

from utils.regex_detector import regex_detector
from utils.presidio_detector import presidio_detector
from utils.deberta_detector import deberta_detector
from utils.spacy_detector import spacy_detector
from utils.merge_results import merge_results
from models.pii_model import PIIResponse

app = FastAPI(title="PII Detection API")

@app.post("/detect", response_model=PIIResponse)
async def detect_pii(text: str = Form(...)):
    # Run all 4 detectors concurrently
    results = await asyncio.gather(
        regex_detector(text),
        presidio_detector(text),
        deberta_detector(text),
        spacy_detector(text)
    )

    merged = merge_results(*results)
    return PIIResponse(text=text, pii_entities=merged)
