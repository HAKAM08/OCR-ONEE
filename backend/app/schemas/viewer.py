from datetime import datetime

from pydantic import BaseModel


class ViewerResponse(BaseModel):

    id: int

    original_filename: str

    filename: str

    file_type: str

    file_path: str

    status: str

    upload_date: datetime

    language: str

    confidence: float

    processing_time: float

    text: str

    class Config:
        from_attributes = True