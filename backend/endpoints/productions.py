from flask_restful import Resource, marshal_with, fields, reqparse
from sqlalchemy_media import StoreManager

from database import db
from models.production import Production


class ReleaseDate(fields.DateTime):
    def format(self, value):
        return str(value)


class Image(fields.Raw):
    def format(self, value):
        with StoreManager(db.session()):
            return value.locate()


class Productions(Resource):
    @marshal_with({
        'pk': fields.Integer,
        'slug': fields.String,
        'title': fields.String,
        'released': ReleaseDate,
        'year': fields.Integer,
        'summary': fields.String,
        'summary_credit': fields.String,
        'runtime': fields.Integer,
        'directors': fields.Nested({
            'pk': fields.Integer,
            'name': fields.String,
            'imdb_id': fields.String,
        }),
        'poster': Image(),
        'tmdb_id': fields.String,
        'imdb_id': fields.String,
        'nbdb_id': fields.String,
    })
    def get(self, slug=None):
        if slug:
            return Production.query.filter_by(slug=slug).first_or_404()

        parser = reqparse.RequestParser()
        parser.add_argument('person', type=str)
        args = parser.parse_args()

        if args['person']:
            return []

        return Production.query.limit(15).all()
