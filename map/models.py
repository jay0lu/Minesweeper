from django.db import models

class Map(models.Model):
  uid = models.CharField(max_length=50, unique=True)
  mineMap = models.CharField(max_length=100)
