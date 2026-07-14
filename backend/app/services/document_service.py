from datetime import UTC, datetime

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.enums.document_status import DocumentStatus
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.services.file_service import FileService


class DocumentService:
    """
    Service responsible for document-related business logic.
    """

    @staticmethod
    def upload_document(
        db: Session,
        file: UploadFile,
        owner_id: int
    ) -> Document:
        """
        Uploads a document and stores its metadata.
        """

        file_data = FileService.save_file(file)

        document = Document(
            original_filename=file_data["original_filename"],
            filename=file_data["filename"],
            file_type=file_data["extension"],
            file_path=file_data["filepath"],
            upload_date=datetime.now(UTC),
            status=DocumentStatus.UPLOADED.value,
            owner_id=owner_id
        )

        return DocumentRepository.create(
            db,
            document
        )

    @staticmethod
    def get_document(
        db: Session,
        document_id: int
    ) -> Document:

        document = DocumentRepository.get_by_id(
            db,
            document_id
        )

        if document is None:
            raise ValueError("Document not found.")

        return document

    @staticmethod
    def get_all_documents(
        db: Session
    ) -> list[Document]:

        return DocumentRepository.get_all(db)

    @staticmethod
    def update_status(
        db: Session,
        document_id: int,
        status: DocumentStatus
    ) -> Document:

        return DocumentRepository.update_status(
            db,
            document_id,
            status.value
        )

    @staticmethod
    def delete_document(
        db: Session,
        document_id: int
    ) -> None:

        document = DocumentRepository.get_by_id(
            db,
            document_id
        )

        if document is None:
            raise ValueError("Document not found.")

        DocumentRepository.delete(
            db,
            document
        )