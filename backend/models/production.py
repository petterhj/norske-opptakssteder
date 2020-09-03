from enum import Enum
from datetime import date
from pydantic import Field, FilePath, validator
from pymongo import IndexModel
from typing import Optional, List
# from slugify import slugify

from .base import MongoDocument
# from .common import SourcesMixin
from .people import Person
# from .fields import AutoSlug


class ProductionType(str, Enum):
    film = "film"
    tv = "tv"


class Production(MongoDocument):
    type: Optional[ProductionType] = None

    title: str = Field(max_length=75)
    release_date: date
    summary: Optional[str] = Field(max_length=500)
    summary_credit: Optional[str] = Field(max_length=30)
    runtime: Optional[int] = Field(ge=0, le=360)

    directors: Optional[List[Person]] = list()

    imdb_id: str = Field(max_length=10)
    tmdb_id: Optional[str] = Field(max_length=10)
    nbdb_id: Optional[str] = Field(max_length=10)

    poster: FilePath = None

    # slug: str = None
    # slug: AutoSlug = Field(..., populate_from="title")

    # @validator("slug", pre=True, always=True)
    # async def slugify(cls, v, values, field, config):
    #     print("^"*10)
    #     print("CLS", cls)
    #     print("V", v)
    #     print("VALUES", values)
    #     print("FIELD",  field)
    #     print("CONFIG", config)
    #     print("^"*10)
    #     slug = slugify(values["title"], to_lower=True)
    #     print(slug)
    #     print("="*10)
    #     p = await cls.find_one({"slug": slug})
    #     print(cls.find_one({"slug": slug}))
    #     print("="*10)
    #     return None

    @validator("poster")
    def path_string(cls, v):
        if v:
            return str(v)

    @property
    def year(self):
        return self.release_date.year

    def dict(self, *args, **kwargs):
        attrs = super().dict(*args, **kwargs)
        attrs.update({"year": self.year})
        return attrs

    class Mongo:
        collection = "productions"
        indexes = [IndexModel("imdb_id", unique=True)]
