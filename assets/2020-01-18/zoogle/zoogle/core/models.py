from uuid import uuid4

from django.db.models import CharField, UUIDField, DateTimeField, Model


class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)
    subject = CharField(max_length=200)
    description = CharField(max_length=400)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.subject}: {self.description}'
