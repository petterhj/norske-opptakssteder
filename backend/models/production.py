from sqlalchemy_media import (
    ImageAnalyzer, ImageValidator, ImageProcessor
)

from .media import Image, ImageJson
from database import db


class ProductionPoster(Image):
    __directory__ = 'posters'
    __prefix__ = 'poster'
    __pre_processors__ = [
        ImageAnalyzer(),
        ImageValidator(
            minimum=(200, 290),
            maximum=(800, 1164),
            min_aspect_ratio=0.6,
            content_types=['image/jpeg', 'image/png']
        ),
        ImageProcessor(
            fmt='jpeg',
            width=120,
        )
    ]


class Production(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), unique=True, nullable=False)

    title = db.Column(db.String(50), nullable=False)
    released = db.Column(db.Date, nullable=False)
    summary = db.Column(db.Text, nullable=True)
    summary_credit = db.Column(db.String(30), nullable=True)
    runtime = db.Column(db.SmallInteger, nullable=True)

    directors = db.relationship('Person', secondary=db.Table(
        'directing',
        db.Column('production_pk', db.Integer, db.ForeignKey('production.pk')),
        db.Column('person_pk', db.Integer, db.ForeignKey('person.pk'))
    ))

    # writers = ManyToManyField('Person', blank=True, related_name='writers')
    # photographers = ManyToManyField('Person', blank=True, related_name='photographers')
    # producers = ManyToManyField('Company', blank=True, related_name='producers')
    # distributors = ManyToManyField('Company', blank=True, related_name='distributors')

    poster = db.Column(ProductionPoster.as_mutable(ImageJson))

    imdb_id = db.Column(db.String(10), unique=True, nullable=False)
    tmdb_id = db.Column(db.String(10), unique=True, nullable=True)
    nbdb_id = db.Column(db.String(10), unique=True, nullable=True)

    @property
    def year(self):
        return self.released.year

    @property
    def title_with_year(self):
        return f'{self.title} ({self.year})'
