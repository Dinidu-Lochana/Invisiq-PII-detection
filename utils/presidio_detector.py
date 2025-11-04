from presidio_analyzer import AnalyzerEngine
from models.pii_model import PIIEntity

analyzer = AnalyzerEngine()

async def presidio_detector(text: str):
    analyzer_results = analyzer.analyze(text=text, language="en")
    results = [
        PIIEntity(
            type=res.entity_type,
            text=text[res.start:res.end],
            start=res.start,
            end=res.end,
            score=res.score,
            source="presidio"
        )
        for res in analyzer_results
    ]
    return results
