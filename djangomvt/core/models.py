from django.db import models
from django.utils import timezone

class BaseEntity(models.Model):
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True