from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    """
    Repository responsible for all database operations
    related to documents.
    """

    @staticmethod
    def create(db: Session, document: Document) -> Document:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_by_id(db: Session, document_id: int) -> Document | None:
        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def get_all(db: Session) -> list[Document]:
        return (
            db.query(Document)
            .order_by(Document.upload_date.desc())
            .all()
        )

    @staticmethod
    def exists(db: Session, document_id: int) -> bool:
        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
            is not None
        )

    @staticmethod
    def update(db: Session, document: Document) -> Document:
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def update_status(
        db: Session,
        document_id: int,
        status: str
    ) -> Document:

        document = DocumentRepository.get_by_id(
            db,
            document_id
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
        file_path: str
    ) -> Document:

        document = DocumentRepository.get_by_id(
            db,
            document_id
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
        document: Document
    ) -> None:

        db.delete(document)

        db.commit()