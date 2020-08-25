from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    displayname = models.CharField(max_length=240, unique=False, default="")
