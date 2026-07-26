from datetime import datetime

from pydantic import BaseModel


class RecentDocument(BaseModel):
    id: int
    filename: str
    status: str
    upload_date: datetime

    class Config:
        from_attributes = True


class LanguageStat(BaseModel):
    language: str
    count: int


class DashboardStats(BaseModel):
    total_documents: int
    ocr_completed: int
    processing: int
    indexed: int
    average_confidence: float
    detected_languages: list[LanguageStat]
    recent_documents: list[RecentDocument]