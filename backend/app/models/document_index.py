
from sqlalchemy import String, DateTime, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class DocumentIndex(Base):

    __tablename__ = "document_indexes"

    id: Mapped[int] = mapped_column(primary_key=True)

    keywords: Mapped[str]

    category: Mapped[str]

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id")
    )

    document = relationship("Document")