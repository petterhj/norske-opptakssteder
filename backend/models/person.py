from pydantic import Field
from typing import Optional
from motor_odm import Document

from .base import MongoDocument
from .common import SourcesMixin


class Person(MongoDocument):
    # slug: str
    name: str = Field(max_length=50)

    bio: Optional[str] = Field(max_length=300)
    # bio_credit: Optional[str] = Field(max_length=30)

    # imdb_id: str = Field(max_length=10)
    # tmdb_id: Optional[str] = Field(max_length=10)
    # nbdb_id: Optional[str] = Field(max_length=10)

    class Mongo:
        collection = "people"


"""
slug = SlugField(populate_from="name", required=True, unique=True,)
# known_for_department = db.Column(db.String(50), nullable=False)
# headshot = db.Column(Headshot.as_mutable(ImageJson))
"""
