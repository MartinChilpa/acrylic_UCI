from django.db import models
from common.models import BaseModel


class Tier(BaseModel):
    name = models.CharField(max_length=100)
    code = models.SlugField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
