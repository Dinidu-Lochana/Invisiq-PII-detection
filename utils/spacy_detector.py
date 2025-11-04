import spacy
from models.pii_model import PIIEntity

nlp = spacy.load("en_core_web_sm")

async def spacy_detector(text: str):
    doc = nlp(text)
    results = [
        PIIEntity(
            type=ent.label_,
            text=ent.text,
            start=ent.start_char,
            end=ent.end_char,
            score=None,
            source="spacy"
        )
        for ent in doc.ents
    ]
    return results
