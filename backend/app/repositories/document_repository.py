from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.user import User
from app.enums.document_type import DocumentType


class DocumentRepository:
    """
    Repository responsible for all database operations
    related to documents.
    """

    @staticmethod
    def create(
        db: Session,
        document: Document,
    ) -> Document:

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int,
    ) -> Document | None:

        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def get_by_id_for_user(
        db: Session,
        document_id: int,
        current_user: User,
    ) -> Document | None:

        query = (
            db.query(Document)
            .filter(Document.id == document_id)
        )

        if current_user.role != "ADMIN":

            query = query.filter(
                Document.document_type == DocumentType.COMMON.value
            )

        return query.first()

    @staticmethod
    def get_all_for_user(
        db: Session,
        current_user: User,
    ) -> list[Document]:

        query = db.query(Document)

        if current_user.role != "ADMIN":

            query = query.filter(
                Document.document_type == DocumentType.COMMON.value
            )

        return (
            query
            .order_by(Document.upload_date.desc())
            .all()
        )

    @staticmethod
    def get_paginated_for_user(
        db: Session,
        current_user: User,
        page: int,
        page_size: int,
    ):

        query = db.query(Document)

        if current_user.role != "ADMIN":

            query = query.filter(
                Document.document_type == DocumentType.COMMON.value
            )

        return (
            query
            .order_by(Document.upload_date.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

    @staticmethod
    def exists(
        db: Session,
        document_id: int,
    ) -> bool:

        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
            is not None
        )

    @staticmethod
    def update(
        db: Session,
        document: Document,
    ) -> Document:

        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def update_status(
        db: Session,
        document_id: int,
        status: str,
    ) -> Document:

        document = DocumentRepository.get_by_id(
            db,
            document_id,
        )

        if document is None:
            raise ValueError("Document not found.")

        document.status = status

        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def update_file_path(
        db: Session,
        document_id: int,
        file_path: str,
    ) -> Document:

        document = DocumentRepository.get_by_id(
            db,
            document_id,
        )

        if document is None:
            raise ValueError("Document not found.")

        document.file_path = file_path

        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def delete(
        db: Session,
        document: Document,
    ) -> None:

        db.delete(document)
        db.commit()