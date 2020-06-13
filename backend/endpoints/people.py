from flask_restful import Resource, marshal_with, fields, reqparse
from sqlalchemy_media import StoreManager

from database import db
from models.person import Person


class ReleaseDate(fields.DateTime):
    def format(self, value):
        return str(value)


class Image(fields.Raw):
    def format(self, value):
        with StoreManager(db.session()):
            return value.locate()


class People(Resource):
    @marshal_with({
        'pk': fields.Integer,
        'slug': fields.String,
        'name': fields.String,
        'bio': fields.String,
        'bio_credit': fields.String,
        'headshot': Image(),
        'tmdb_id': fields.String,
        'imdb_id': fields.String,
    })
    def get(self, slug=None):
        if slug:
            return Person.query.filter_by(slug=slug).first_or_404()

        parser = reqparse.RequestParser()
        parser.add_argument('department', type=str)
        args = parser.parse_args()

        if args['department']:
            return Person.query.filter_by(
                known_for_department=args['department']
            ).all()

        return Person.query.all()
