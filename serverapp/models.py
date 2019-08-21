from django.db import models
from django.contrib.auth.models import User


class Paper(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


