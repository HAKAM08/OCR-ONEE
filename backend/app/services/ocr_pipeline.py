from app.database.database import SessionLocal
from app.enums.document_status import DocumentStatus
from app.models.ocr_result import OCRResult

from app.repositories.document_repository import DocumentRepository
from app.repositories.ocr_result_repository import OCRResultRepository

from app.schemas import document
from app.services.converters.document_conversion_service import (
    DocumentConversionService,
)
from app.services.ocr_service import OCRService
from app.elasticsearch.index_service import IndexService

class OCRPipeline:
    """
    Complete OCR processing pipeline.

    Workflow:

        Retrieve document
                │
                ▼
        Convert document to images
                │
                ▼
        OCR Engine
                │
                ▼
        Save OCR Result
                │
                ▼
        Update document status
    """

    @staticmethod
    def process(document_id: int) -> OCRResult:

        db = SessionLocal()

        try:

            # ----------------------------
            # Retrieve document
            # ----------------------------

            document = DocumentRepository.get_by_id(
                db,
                document_id
            )

            if document is None:
                raise ValueError("Document not found.")

            # ----------------------------
            # Update status
            # ----------------------------

            DocumentRepository.update_status(
                db,
                document.id,
                DocumentStatus.PROCESSING.value
            )

            # ----------------------------
            # Convert document
            # ----------------------------

            images = DocumentConversionService.convert(
                document.file_path
            )

            # ----------------------------
            # OCR Engine
            # ----------------------------

            result = OCRService.process_images(
                images
            )

            # ----------------------------
            # Save OCR Result
            # ----------------------------

            ocr_result = OCRResult(

                text=result.text,

                confidence=result.confidence,

                language=result.language,

                processing_time=result.processing_time,

                page_count=result.page_count,

                engine_version="Tesseract 5",

                document_id=document.id

            )

            OCRResultRepository.create(
                db,
                ocr_result
            )
            
            # ----------------------------
            # Index document in Elasticsearch
            # ----------------------------

            IndexService.index_document(
                document,
                ocr_result
            )

            # ----------------------------
            # Update document status
            # ----------------------------

            DocumentRepository.update_status(
                db,
                document.id,
                DocumentStatus.OCR_COMPLETED.value
            )

            return ocr_result

        except Exception:

            if "document" in locals():

                DocumentRepository.update_status(
                    db,
                    document.id,
                    DocumentStatus.FAILED.value
                )

            raise

        finally:

            db.close()