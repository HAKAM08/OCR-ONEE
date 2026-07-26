
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class SearchHistory(Base):

    __tablename__ = "search_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    keyword: Mapped[str]

    search_date: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user = relationship("User")