from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository
from app.schemas.dashboard import DashboardStats


class DashboardService:
    """
    Service responsible for building the complete
    dashboard response.
    """

    @staticmethod
    def get_dashboard_stats(
        db: Session
    ) -> DashboardStats:

        total_documents = (
            DashboardRepository.get_total_documents(db)
        )

        ocr_completed = (
            DashboardRepository.get_completed_documents(db)
        )

        processing = (
            DashboardRepository.get_processing_documents(db)
        )

        indexed = (
            DashboardRepository.get_indexed_documents(db)
        )

        average_confidence = (
            DashboardRepository.get_average_confidence(db)
        )

        detected_languages = (
            DashboardRepository.get_detected_languages(db)
        )

        recent_documents = (
            DashboardRepository.get_recent_documents(db)
        )

        return DashboardStats(

            total_documents=total_documents,

            ocr_completed=ocr_completed,

            processing=processing,

            indexed=indexed,

            average_confidence=average_confidence,

            detected_languages=detected_languages,

            recent_documents=recent_documents

        )