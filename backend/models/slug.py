from pymongo import IndexModel

from .base import MongoDocument


class Slug(MongoDocument):
    slug: str
    object_id: str

    class Mongo:
        collection = "slugs"
        indexes = [IndexModel("slug", unique=True)]
