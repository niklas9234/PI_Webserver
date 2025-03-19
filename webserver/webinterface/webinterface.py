import logging

from flask import Flask, g

from webserver.webinterface.routes.example_blueprint import example_blueprint



class Webinterface:
    def __init__(self, db):
        self.app = Flask(__name__, template_folder="templates")
        self.app.config.from_mapping(SECRET_KEY='dev')
        self._logger = logging.getLogger("webserver")
        self.setup_session_handling()
        self.register_blueprints()
        self._db = db


    def setup_session_handling(self):
        @self.app.before_request
        def start_session():
            g.db_session = next(self._db.get_db_session())

        @self.app.teardown_request
        def close_session(exception=None):
            db_session = getattr(g, "db_session", None)
            if db_session:
                db_session.commit()
                db_session.close()


    def register_blueprints(self):
        self.app.register_blueprint(example_blueprint)


    def run(self, host="0.0.0.0", port=5000, debug=True):
        self.app.run(host=host, port=port, debug=debug)

