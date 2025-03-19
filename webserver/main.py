import logging
import os

from dotenv import load_dotenv

from logging_config import LoggingConfig
from webserver.database.database import Database
from webserver.webinterface.webinterface import Webinterface

load_dotenv()


def main():

    LoggingConfig.setup_logging()
    logger = logging.getLogger("webserver")
    logger.info("--- Webserver startup ---")

    db = Database(f'postgresql://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}'
                  f'@{os.getenv("DATABASE_URI")}/{os.getenv("DATABASE_NAME")}')

    web_app = Webinterface(db)
    web_app.run()




if __name__ == "__main__":
    main()