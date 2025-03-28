from __future__ import annotations

from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship, WriteOnlyMapped
from werkzeug.security import generate_password_hash, check_password_hash

from webserver.database.base import Base
#from webserver.database.models.posting import Posting


class User(Base, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64),index=True, unique=True)
    password: Mapped[str] = mapped_column(String(256))
    role: Mapped[str] = mapped_column(default="user")
    is_active: Mapped[bool] = mapped_column(default=True)
    last_login: Mapped[datetime] = mapped_column(default=datetime.now)

    posts: WriteOnlyMapped['Posting'] = relationship(back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, _password):
        self.password = generate_password_hash(_password)

    def check_password(self, _password):
        return check_password_hash(self.password, _password)

