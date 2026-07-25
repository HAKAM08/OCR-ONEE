from app.database.database import SessionLocal

from app.enums.document_status import DocumentStatus

from app.models.ocr_result import OCRResult

from app.repositories.document_repository import DocumentRepository
from app.repositories.ocr_result_repository import OCRResultRepository

from app.services.converters.document_conversion_service import (
    DocumentConversionService,
)

from app.services.docx_service import DOCXService
from app.services.ocr_correction_service import OCRCorrectionService
from app.services.language_detection_service import LanguageDetectionService
from app.services.ocr_service import OCRService

from app.core.ocr.ocr_processing_result import OCRProcessingResult

from app.elasticsearch.index_service import IndexService


class OCRPipeline:
    """
    Complete OCR processing pipeline.

    Images / PDFs
        -> Convert to images
        -> OCR
        -> AI correction

    DOCX
        -> Extract text
        -> AI correction
    """

    @staticmethod
    def process(document_id: int) -> OCRResult:

        db = SessionLocal()

        try:

            document = DocumentRepository.get_by_id(
                db,
                document_id,
            )

            if document is None:
                raise ValueError("Document not found.")

            DocumentRepository.update_status(
                db,
                document.id,
                DocumentStatus.PROCESSING.value,
            )

            extension = document.file_type.lower()

            # ===================================================
            # DOCX
            # ===================================================

            if extension == ".docx":

                text = DOCXService.extract_text(
                    document.file_path
                )

                result = OCRProcessingResult(

                    text=text,

                    confidence=100.0,

                    language=LanguageDetectionService.detect(
                        text
                    ),

                    processing_time=0,

                    page_count=1,

                )

            # ===================================================
            # PDF / Images
            # ===================================================

            else:

                images = DocumentConversionService.convert(
                    document.file_path
                )

                result = OCRService.process_images(
                    images
                )

            # ===================================================
            # Save OCR Result
            # ===================================================

            ocr_result = OCRResult(

                text=result.text,

                confidence=result.confidence,

                language=result.language,

                processing_time=result.processing_time,

                page_count=result.page_count,

                engine_version="Tesseract 5",

                document_id=document.id,

            )

            OCRResultRepository.create(
                db,
                ocr_result,
            )

            # ===================================================
            # Elasticsearch
            # ===================================================

            IndexService.index_document(
                document,
                ocr_result,
            )

            # ===================================================
            # Completed
            # ===================================================

            DocumentRepository.update_status(
                db,
                document.id,
                DocumentStatus.OCR_COMPLETED.value,
            )

            return ocr_result

        except Exception:

            if "document" in locals():

                DocumentRepository.update_status(
                    db,
                    document.id,
                    DocumentStatus.FAILED.value,
                )

            raise

        finally:

            db.close()