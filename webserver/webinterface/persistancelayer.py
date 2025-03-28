from typing import Optional

from flask_login import LoginManager

from webserver.database.database import Database


class PersistenceLayer:
    _db: Optional[Database] = None


    @classmethod
    def init_database(cls, db) -> None:
        cls._db = db

    @classmethod
    def db(cls) -> Database:
        if cls._db is None:
            raise Exception("Persistance Layer not initialized")
        return cls._db


