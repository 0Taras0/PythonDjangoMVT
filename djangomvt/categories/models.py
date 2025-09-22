from django.db import models

from core.models import BaseEntity


class Category(BaseEntity):
    name = models.CharField(max_length=250, default="", blank=False)
    image = models.CharField(max_length=200, default="", blank=True)
    slug = models.SlugField(max_length=250, unique=True, default="")
    
    def __str__(self):
        return self.name