from sqlalchemy.orm import Session

from app.models.ocr_result import OCRResult


class OCRResultRepository:
    """
    Repository responsable des opérations CRUD
    sur les résultats OCR.
    """

    @staticmethod
    def create(db: Session, ocr_result: OCRResult) -> OCRResult:
        db.add(ocr_result)
        db.commit()
        db.refresh(ocr_result)
        return ocr_result

    @staticmethod
    def get_by_document_id(
        db: Session,
        document_id: int
    ) -> OCRResult | None:

        return (
            db.query(OCRResult)
            .filter(
                OCRResult.document_id == document_id
            )
            .first()
        )

    @staticmethod
    def update(db: Session, ocr_result: OCRResult) -> OCRResult:
        db.commit()
        db.refresh(ocr_result)
        return ocr_result

    @staticmethod
    def delete(db: Session, ocr_result: OCRResult) -> None:
        db.delete(ocr_result)
        db.commit()