# from flask_restful import fields
from sqlalchemy_media import (
    ImageAnalyzer, ImageValidator, ImageProcessor  # , StoreManager
)

from .media import Image, ImageJson
from database import db


class Headshot(Image):
    __directory__ = 'headshots'
    __prefix__ = 'headshot'
    __pre_processors__ = [
        ImageAnalyzer(),
        ImageValidator(
            minimum=(200, 200),
            maximum=(800, 800),
            content_types=['image/jpeg', 'image/png']
        ),
        ImageProcessor(
            fmt='jpeg',
            width=500,
        )
    ]


class Person(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), unique=True, nullable=False)

    name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    bio_credit = db.Column(db.String(30), nullable=True)
    known_for_department = db.Column(db.String(50), nullable=False)

    headshot = db.Column(Headshot.as_mutable(ImageJson))

    imdb_id = db.Column(db.String(10), unique=True, nullable=False)
    tmdb_id = db.Column(db.String(10), unique=True, nullable=True)
