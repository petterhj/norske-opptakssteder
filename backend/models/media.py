import json
from sqlalchemy_media import Image

from database import db


class ImageJson(db.TypeDecorator):
    impl = db.Unicode

    def process_bind_param(self, value, engine):
        return json.dumps(value)

    def process_result_value(self, value, engine):
        if value is None:
            return None

        return json.loads(value)


class Image(Image):
    def locate(self):
        return self.get_store().locate(self)

    @property
    def suffix(self):
        return ''