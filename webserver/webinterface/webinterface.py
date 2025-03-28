import logging
from typing import Optional


from flask import Flask, g
from flask_login import LoginManager

from webserver.database.database import Database
from webserver.database.models.user import User
from webserver.webinterface.auth import auth_bp
from webserver.webinterface.blog import blog_bp
from webserver.webinterface.config import Config
from webserver.webinterface.persistancelayer import PersistenceLayer


class Webinterface:
    _db: Optional[Database] = None
    def __init__(self):
        self.app = Flask(__name__, template_folder="templates")
        self.app.config.from_object(Config)
        self._logger = logging.getLogger("webserver")

        self.register_blueprints()
        self.create_user_loader()

        @self.app.route('/test/')
        def test_page():
            return '<h1>Testing the Flask Application Factory Pattern</h1>'


    def create_user_loader(self):
        login = LoginManager(self.app)
        login.login_view = 'login'
        @login.user_loader
        def load_user(_id):
            with PersistenceLayer.db().get_db_session() as db_session:
                return db_session.get(User, int(_id))

    def register_blueprints(self):
        self.app.register_blueprint(auth_bp)
        self.app.register_blueprint(blog_bp)


    def run(self, host="0.0.0.0", port=5000, debug=True):
        self.app.run(host=host, port=port, debug=debug)

