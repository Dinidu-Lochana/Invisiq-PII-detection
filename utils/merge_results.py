from typing import List
from models.pii_model import PIIEntity

def merge_results(*detector_outputs: List[PIIEntity]) -> List[PIIEntity]:
    merged = []
    seen = set()
    for output in detector_outputs:
        for ent in output:
            key = (ent.text.lower(), ent.start, ent.end)
            if key not in seen:
                seen.add(key)
                merged.append(ent)
    return merged
