from django.db import models
from random import randint

col = 10
row = 10
mine = 10
mineLocation = []
def generateMap():
  limit = col * row
  i = 0
  while i < mine:
    location = randint(0, limit)
    if not (location in mineLocation):
      mineLocation.append(location)
      i += 1


class map(models.Model):
  uid = models.CharField(max_length=300, unique=True)
  mine = models.CharField()
