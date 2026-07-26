from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.ocr_result import OCRResult


class DashboardRepository:
    """
    Repository responsible for retrieving all
    dashboard statistics from PostgreSQL.
    """

    @staticmethod
    def get_total_documents(db: Session) -> int:
        return db.query(Document).count()

    @staticmethod
    def get_completed_documents(db: Session) -> int:
        return (
            db.query(Document)
            .filter(
                Document.status == "OCR_COMPLETED"
            )
            .count()
        )

    @staticmethod
    def get_processing_documents(db: Session) -> int:
        return (
            db.query(Document)
            .filter(
                Document.status == "PROCESSING"
            )
            .count()
        )

    @staticmethod
    def get_indexed_documents(db: Session) -> int:
        return (
            db.query(OCRResult)
            .count()
        )

    @staticmethod
    def get_average_confidence(db: Session) -> float:

        value = (
            db.query(
                func.avg(
                    OCRResult.confidence
                )
            )
            .scalar()
        )

        if value is None:
            return 0.0

        return round(float(value), 2)

    @staticmethod
    def get_detected_languages(db: Session):

        rows = (
        db.query(
            OCRResult.language,
            func.count(OCRResult.id).label("count"),
        )
        .group_by(OCRResult.language)
        .all()
    )

        return [
        {
            "language": language,
            "count": count,
        }
        for language, count in rows
    ]

    @staticmethod
    def get_recent_documents(
        db: Session,
        limit: int = 5
    ):
        return (
            db.query(Document)
            .order_by(
                Document.upload_date.desc()
            )
            .limit(limit)
            .all()
        )