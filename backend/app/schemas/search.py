from pydantic import BaseModel


class SearchResult(BaseModel):
    """
    Search result returned to the frontend.
    """

    document_id: int

    filename: str

    confidence: float

    page_count: int

    score: float

    highlights: list[str]