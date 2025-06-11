import uuid

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    balance = models.IntegerField()
