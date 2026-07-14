from datetime import datetime, UTC

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class OCRResult(Base):

    __tablename__ = "ocr_results"

    id: Mapped[int] = mapped_column(primary_key=True)

    text: Mapped[str] = mapped_column(Text)

    confidence: Mapped[float] = mapped_column(Float)

    language: Mapped[str] = mapped_column(
        String(20)
    )

    processing_time: Mapped[float] = mapped_column(
        Float
    )

    page_count: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    engine_version: Mapped[str] = mapped_column(
        String(50),
        default="Tesseract 5"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id"),
        unique=True
    )

    document = relationship("Document")