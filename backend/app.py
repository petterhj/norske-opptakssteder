from flask import Flask
from flask_cors import CORS

from database import db, migrate
from api import norloc_api


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('./config.cfg')

    norloc_api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    CORS(app)

    return app
