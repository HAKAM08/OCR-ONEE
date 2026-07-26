from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.ocr_pipeline import OCRPipeline

router = APIRouter(
    prefix="/ocr",
    tags=["OCR"]
)


@router.post("/{document_id}")
def process_document(
    document_id: int,
    db: Session = Depends(get_db)
):

    result = OCRPipeline.process(
        db,
        document_id
    )

    return result