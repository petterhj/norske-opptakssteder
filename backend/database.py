import os
from functools import partial
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_media import StoreManager, FileSystemStore


db = SQLAlchemy()
migrate = Migrate()


TEMP_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

StoreManager.register(
    'fs',
    partial(FileSystemStore, TEMP_PATH, 'http://localhost:5000/static/'),
    default=True
)