import os
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from webserver.database.base import Base
from webserver.database.models.user import User


class Posting(Base):
    __tablename__ = "posting"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_on: Mapped[datetime] = mapped_column(index=True, default=datetime.now)
    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id),index=True)

    author: Mapped[User] = relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def to_dict(self):
        return {
            "id": self.id,
            "created_on": self.created_on.strftime(os.getenv('CUSTOM_DATE_TIME')) if self.created_on else None,
            "title": self.title,
            "body": self.body,
            "author": self.author.username if self.author else None,
        }