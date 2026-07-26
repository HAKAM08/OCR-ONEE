from dataclasses import dataclass


@dataclass
class OCRProcessingResult:
    """
    Represents the final OCR result.
    """

    text: str

    confidence: float

    processing_time: float

    page_count: int

    language: str