from django.db import models

class Map(models.Model):
  uid = models.CharField(max_length=50, unique=True)
  mineMap = models.CharField(max_length=1000)
  currentMap = models.CharField(max_length=1000)
