from django.db.models import EmailField

from zoogle.core.models import BaseModel


class Zmail(BaseModel):
    from_addr = EmailField()
    to_addr = EmailField()
