import os

from dotenv import load_dotenv

from webserver.database.database import Database
from webserver.webinterface.persistancelayer import PersistenceLayer
from webserver.webinterface.webinterface import Webinterface

load_dotenv()


def main():
    PersistenceLayer.init_database(Database(
        f'postgresql://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}'
        f'@{os.getenv("DATABASE_URI")}/{os.getenv("DATABASE_NAME")}'
    ))

    web_app = Webinterface()
    web_app.run()


if __name__ == "__main__":
    main()