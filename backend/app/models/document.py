from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.enums.document_type import DocumentType


class Document(Base):

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)

    original_filename: Mapped[str] = mapped_column(
        String(255)
    )

    filename: Mapped[str] = mapped_column(
        String(255)
    )

    file_type: Mapped[str] = mapped_column(
        String(50)
    )

    file_path: Mapped[str] = mapped_column(
        String(500)
    )

    upload_date: Mapped[datetime] = mapped_column(
        DateTime
    )

    status: Mapped[str] = mapped_column(
        String(30)
    )

    document_type: Mapped[str] = mapped_column(
        String(30),
        default=DocumentType.COMMON.value
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    owner = relationship("User")