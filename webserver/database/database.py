import logging

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

from webserver.database.base import  Base


class Database:

    def __init__(self, db_url:str):
        self.logger = logging.getLogger("webserver")
        self.logger.info("--- Init Database ---")
        try:
            if not database_exists(db_url):
                create_database(db_url)

            self.engine = create_engine(db_url, pool_size=20, max_overflow=0, echo=False)
            self.connection = self.engine.connect()

            Base.metadata.create_all(self.engine)

            self.SessionFactory = sessionmaker(bind=self.engine)
            self.Session = scoped_session(self.SessionFactory)

        except Exception:
            self.logger.exception(f'Database Connection error')
            raise Exception

    def get_db_session(self):
        db_session = self.Session()
        try:
            yield db_session
        finally:
            db_session.close()


    def connection_status(self):
        inspection = inspect(self.engine)
        return f'Connection on "{self.engine.url}" with Tables {inspection.get_table_names()}'
