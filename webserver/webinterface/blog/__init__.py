from flask import Blueprint

blog_bp = Blueprint('blog', __name__)

from .routes import my_posts
from .routes import explore
from .routes import create