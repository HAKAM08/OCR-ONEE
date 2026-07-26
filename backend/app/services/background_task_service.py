from fastapi import BackgroundTasks

from app.services.ocr_pipeline import OCRPipeline


class BackgroundTaskService:
    """
    Centralized service responsible for scheduling
    background jobs.
    """

    @staticmethod
    def start_document_processing(
        background_tasks: BackgroundTasks,
        document_id: int
    ) -> None:

        background_tasks.add_task(
            OCRPipeline.process,
            document_id
        )