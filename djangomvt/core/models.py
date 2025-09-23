from django.db import models
from django.utils import timezone

class BaseEntity(models.Model):
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True