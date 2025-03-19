from sqlalchemy.orm import mapped_column, Mapped

from webserver.database.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(default="user")
    is_active: Mapped[bool] = mapped_column(default=True)
    last_login: Mapped[str] = mapped_column()

    def __repr__(self):
        return '<User %r>' % self.name

