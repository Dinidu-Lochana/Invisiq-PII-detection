from transformers import pipeline
from models.pii_model import PIIEntity

# Load Hugging Face NER model
nlp = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")



async def deberta_detector(text: str):
    entities = nlp(text)
    results = [
        PIIEntity(
            type=ent["entity_group"],
            text=ent["word"],
            start=ent["start"],
            end=ent["end"],
            score=ent["score"],
            source="deberta"
        )
        for ent in entities
    ]
    return results
