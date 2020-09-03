from pydantic.fields import FieldInfo
from slugify import slugify


# class SlugField(FieldInfo):
#     def __init__(self, populate_from, *args, **kwargs):
#         # self.default = default
#         # self.default_factory = kwargs.pop('default_factory', None)
#         print("INIT")
#         print(args)
#         print(kwargs)
#         super().__init__(self, *args, **kwargs)


class AutoSlug(str):
    def __init__(self, *args, **kwargs):
        print("INIT")

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.slugify
        yield cls.unique

    @classmethod
    def slugify(cls, v, values, field, config):
        print("SLUGIFY")
        populate_from = field.field_info.extra.get("populate_from")
        
        assert populate_from, "populate_from not defined"
        assert populate_from in values, \
            f"field \"{populate_from}\" for populate_from not found"

        populate_value = values[populate_from]

        assert populate_value, "no value to populate from"

        slug = slugify(populate_value, to_lower=True)

        print(slug)
        print("---"*5)
        print("CLS", cls)
        print("VAL", v)
        print("VALUES", values)
        print("CONFIG", config)
        print("~"*5)
        print("FIELD", field)
        print("FIELD > CLASS", field.__class__)
        print("FIELD > OUTER", field.outer_type_)
        print("FIELD > INFO", field.field_info)
        print("FIELD > CONFIG", field.model_config)
        print("FIELD > VALIDAT", field.validators)
        print("FIELD > PRE_VAL", field.pre_validators)
        print("FIELD > PST_VAL", field.post_validators)
        print("FIELD > SUB_FLDS", field.sub_fields)
        print("FIELD > SHAPE", field.shape)
        print("~"*5)
        print(dir(config))
        
        # if not isinstance(v, str):
        #     raise TypeError('string required')
        # m = post_code_regex.fullmatch(v.upper())
        # if not m:
        #     raise ValueError('invalid postcode format')
        # you could also return a string here which would mean model.post_code
        # would be a string, pydantic won't care but you could end up with some
        # confusion since the value's type won't match the type annotation
        # exactly

        return cls(slug)

    @classmethod
    def unique(cls, v, values, field, config):
        print("UNIQUE")
        print("---"*5)
        print("CLS", cls)
        print("VAL", v)
        print("VALUES", values)
        print("CONFIG", config)
        print("~"*5)
        return cls(v)

    def __repr__(self):
        return f"Slug({super().__repr__()})"



"""
# from mongoengine.errors import ValidationError
from mongoengine.fields import StringField
from mongoengine import signals
from slugify import Slugify


class SlugField(StringField):
    def __init__(self, *args, **kwargs):
        self.populate_from = kwargs.pop("populate_from")

        if isinstance(self.populate_from, str):
            self.populate_from = (self.populate_from,)

        self.always_update = kwargs.pop("always_update", False)

        self._slugify = Slugify(to_lower=True)

        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        signals.pre_save.connect(self._create_slug_signal, sender=owner)

        return super().__get__(instance, owner)

    def _generate_slug(self, document):
        populate_from_values = tuple(
            str(getattr(document, f)) for f in self.populate_from
        )

        attempts = 1
        numeric_increment = 2
        slug = slug_attempt = self._slugify(populate_from_values[0])
        queryset_manager = document.__class__.objects

        while queryset_manager(**{self.db_field: slug}).count() > 0:
            base = "-".join(populate_from_values[:attempts])
            if attempts <= len(populate_from_values):
                slug_attempt = base
            else:
                slug_attempt = f"{base}-{numeric_increment}"
                numeric_increment += 1

            slug = self._slugify(slug_attempt)

            attempts += 1

        return slug

    def _create_slug_signal(self, sender, document, **kwargs):
        if document.pk and not self.always_update:
            return

        slug = self._generate_slug(document)

        document._data[self.name] = slug
        document._mark_as_changed(self.db_field)
"""