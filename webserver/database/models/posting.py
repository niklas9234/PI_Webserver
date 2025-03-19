from sqlalchemy import DateTime, Column
from sqlalchemy.orm import mapped_column, Mapped

from webserver.database.base import Base


class Posting(Base):
    __tablename__ = "posting"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author_id: Mapped[int]
    created: Mapped[DateTime] = Column(DateTime(timezone=True))
    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()




