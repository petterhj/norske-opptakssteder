from bson import ObjectId
from datetime import date
from motor_odm import Document
from pymongo.errors import DuplicateKeyError

# from pydantic import BaseModel, Field


class MongoDocument(Document):
    def dict(self, *args, **kwargs):
        # kwargs["by_alias"] = False

        return super().dict(*args, **kwargs)

    def mongo(self, *args, **kwargs):
        to_save = super().mongo(*args, **kwargs)

        for field, value in to_save.items():
            print(field, value)
            # Store dates as string; not encodeable by bson
            if isinstance(value, date):
                to_save[field] = value.isoformat()

        return to_save

    async def insert(self, *args, **kwargs):
        try:
            result = await self.collection().insert_one(
                self.mongo(), *args, **kwargs
            )
            self.id = result.inserted_id

        except DuplicateKeyError:
            raise

        return self

    @classmethod
    async def all(cls):
        async for doc in cls.find():
            yield doc

    @classmethod
    async def find_by_id(cls, object_id: str):
        return await cls.find_one({"_id": ObjectId(object_id)})

    class Mongo:
        collection = None

    class Config:
        extra = "ignore"
        validate_assignment = True
        # arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda v: str(v),
        }
