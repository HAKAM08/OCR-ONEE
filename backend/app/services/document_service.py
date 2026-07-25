from datetime import UTC, datetime

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.enums.document_status import DocumentStatus
from app.enums.document_type import DocumentType
from app.models.document import Document
from app.models.user import User
from app.repositories.document_repository import DocumentRepository
from app.repositories.ocr_result_repository import OCRResultRepository
from app.services.file_service import FileService


class DocumentService:
    """
    Service responsible for document-related business logic.
    """

    @staticmethod
    def upload_document(
        db: Session,
        file: UploadFile,
        owner_id: int,
        document_type: DocumentType,
    ) -> Document:

        file_data = FileService.save_file(file)

        document = Document(
            original_filename=file_data["original_filename"],
            filename=file_data["filename"],
            file_type=file_data["extension"],
            file_path=file_data["filepath"],
            upload_date=datetime.now(UTC),
            status=DocumentStatus.UPLOADED.value,
            owner_id=owner_id,
            document_type=document_type.value,
        )

        return DocumentRepository.create(
            db,
            document,
        )

    @staticmethod
    def get_document(
        db: Session,
        document_id: int,
        current_user: User,
    ) -> Document:

        document = DocumentRepository.get_by_id_for_user(
            db,
            document_id,
            current_user,
        )

        if document is None:
            raise ValueError(
                "Document not found or access denied."
            )

        return document

    @staticmethod
    def get_all_documents(
        db: Session,
        current_user: User,
    ) -> list[Document]:

        return DocumentRepository.get_all_for_user(
            db,
            current_user,
        )

    @staticmethod
    def get_paginated_documents(
        db: Session,
        current_user: User,
        page: int,
        page_size: int,
    ):

        return DocumentRepository.get_paginated_for_user(
            db,
            current_user,
            page,
            page_size,
        )

    @staticmethod
    def update_status(
        db: Session,
        document_id: int,
        status: DocumentStatus,
    ) -> Document:

        return DocumentRepository.update_status(
            db,
            document_id,
            status.value,
        )

    @staticmethod
    def delete_document(
        db: Session,
        document_id: int,
    ) -> None:

        document = DocumentRepository.get_by_id(
            db,
            document_id,
        )

        if document is None:
            raise ValueError("Document not found.")

        OCRResultRepository.delete_by_document_id(
            db,
            document_id,
        )

        DocumentRepository.delete(
            db,
            document,
        )