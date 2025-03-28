from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from .routes import login
from .routes import dashboard
from .routes import register

