import re
from models.pii_model import PIIEntity

PATTERNS = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "phone": r"\b\d{10,15}\b",
    "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
    "date": r"\b\d{2,4}[-/]\d{1,2}[-/]\d{2,4}\b",
}

async def regex_detector(text: str):
    results = []
    for label, pattern in PATTERNS.items():
        for match in re.finditer(pattern, text):
            results.append(
                PIIEntity(
                    type=label,
                    text=match.group(),
                    start=match.start(),
                    end=match.end(),
                    score=None,
                    source="regex"
                )
            )
    return results
