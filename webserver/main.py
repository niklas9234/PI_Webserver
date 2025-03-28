import logging
import os

from dotenv import load_dotenv
from sqlalchemy import select

from logging_config import LoggingConfig
from webserver.database.database import Database
from webserver.database.models.posting import Posting
from webserver.database.models.user import User
from webserver.webinterface.auth.forms import LoginForm
from webserver.webinterface.persistancelayer import PersistenceLayer
from webserver.webinterface.webinterface import Webinterface

load_dotenv()


def main():

    LoggingConfig.setup_logging()
    logger = logging.getLogger("webserver")
    logger.info("--- Webserver startup ---")

    PersistenceLayer.init_database(Database(
        f'postgresql://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}'
        f'@{os.getenv("DATABASE_URI")}/{os.getenv("DATABASE_NAME")}'
    ))

    web_app = Webinterface()
    web_app.run()





    #user = User(username='admin', role='admin', is_active=True, last_login='2022-12-27 08:26:49.219717')
    #user.set_password('admin')
    #with PersistenceLayer.db().get_db_session() as db_session:
        #db_session.add(user)
        #db_session.commit()

    #with PersistenceLayer.db().get_db_session() as db_session:
    #    new_posting = Posting(title='other next next title', body='My new posting3!', user_id=14)
    #    db_session.add(new_posting)
    #    db_session.commit()



if __name__ == "__main__":
    main()