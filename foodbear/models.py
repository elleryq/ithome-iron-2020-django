from django.db import models
from model_utils.managers import InheritanceManager, JoinManager


class Place(models.Model):
    objects = InheritanceManager()
    objects2 = JoinManager()
    name = models.CharField(max_length=256)


class Restaurant(Place):
    chef = models.CharField(max_length=32)


class Bar(Place):
    bartender = models.CharField(max_length=32)

