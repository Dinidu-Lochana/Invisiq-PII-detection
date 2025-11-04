from pydantic import BaseModel
from typing import List, Optional

class PIIEntity(BaseModel):
    type: str
    text: str
    start: int
    end: int
    score: Optional[float] = None
    source: str

class PIIResponse(BaseModel):
    text: str
    pii_entities: List[PIIEntity]
