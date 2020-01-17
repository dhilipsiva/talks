from django.db.models import IntegerField, CharField

from zoogle.core.models import BaseModel


class Zdoc(BaseModel):
    size = IntegerField()
    owner = CharField(max_length=100)
