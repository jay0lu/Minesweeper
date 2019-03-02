from django.db import models
from random import randint

def generateMap(col, row, mine):
  col = col
  row = row
  mine = mine

  col = 10
  row = 10
  mine = 10

  limit = col * row

  mineLocation = generateMines(mine, limit)

# random generate mines
def generateMines(mine, limit):
  mineLocation = []

  i = 0
  while i < mine:
    location = randint(0, limit)
    if not (location in mineLocation):
      mineLocation.append(location)
      i += 1

  mineLocation.sort()
  mineInsertMap = insertMine(mineLocation)
  return mineInsertMap

# According to the mineLocation, generate map
def insertMine(list):
  i = 0
  board = []
  for i in limit:
    if i in list:
      # 9 indicate
      board.append(9)
    else:
      board.append(0)
  return board

# Adding 1 to the mine surroundings
def plus(list):
  

class map(models.Model):
  uid = models.CharField(max_length=50, unique=True)
  mineMap = models.CharField(max_length=limit)
