from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    nameCompleto = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    shield = models.ImageField(upload_to = "assets/shield")
    imagemCamisa = models.ImageField(upload_to = "assets/shirts")

