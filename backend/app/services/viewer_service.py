from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository
from app.repositories.ocr_result_repository import OCRResultRepository

from app.schemas.viewer import ViewerResponse


class ViewerService:

    @staticmethod
    def get_document(
        db: Session,
        document_id: int
    ) -> ViewerResponse:

        document = DocumentRepository.get_by_id(
            db,
            document_id
        )

        if document is None:
            raise ValueError("Document not found.")

        ocr = OCRResultRepository.get_by_document_id(
            db,
            document_id
        )

        if ocr is None:
            raise ValueError("OCR result not found.")

        return ViewerResponse(

            id=document.id,

            original_filename=document.original_filename,

            filename=document.filename,

            file_type=document.file_type,

            file_path=f"/uploads/documents/{document.filename}",

            status=document.status,

            upload_date=document.upload_date,

            language=ocr.language,

            confidence=ocr.confidence,

            processing_time=ocr.processing_time,

            text=ocr.text

        )