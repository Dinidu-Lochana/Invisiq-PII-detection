from transformers import pipeline
from models.pii_model import PIIEntity

# Load Hugging Face NER model
nlp = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

# PIIs
PII_LABELS = {"PER", "ORG", "LOC"}

async def deberta_detector(text: str):
    entities = nlp(text)

    # Filter out only PII entities
    filtered_entities = [ent for ent in entities if ent["entity_group"] in PII_LABELS]

    results = [
        PIIEntity(
            type=ent["entity_group"],
            text=ent["word"],
            start=ent["start"],
            end=ent["end"],
            score=ent["score"],
            source="deberta"
        )
        for ent in filtered_entities
    ]
    return results
