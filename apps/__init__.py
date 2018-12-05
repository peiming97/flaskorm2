from flask import Flask

from apps.ext import init_ext, init_db
from apps.orm.views import orm


def create_app():
    app = Flask(__name__)
    register(app)
    app.debug = True
    # init_db(app)
    # init_ext(app)
    return app

def register(app:Flask):
    app.register_blueprint(orm)