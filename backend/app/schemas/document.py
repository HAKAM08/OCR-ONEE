from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    file_path: str
    upload_date: datetime
    status: str
    owner_id: int
    document_type: str

    model_config = ConfigDict(
        from_attributes=True
    )