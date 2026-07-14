from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class Document(Base):

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    original_filename: Mapped[str] = mapped_column(String(255))

    filename: Mapped[str] = mapped_column(String(255))

    file_type: Mapped[str] = mapped_column(String(50))

    file_path: Mapped[str] = mapped_column(String(500))

    upload_date: Mapped[datetime] = mapped_column(DateTime)

    status: Mapped[str] = mapped_column(String(30))

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    owner = relationship("User")