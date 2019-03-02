from django.db import models
from random import randint

class Map(models.Model):
  uid = models.CharField(max_length=50, unique=True)
  mineMap = models.CharField(max_length=100)


# def generateMap(col, row, mine):
#   col = col
#   row = row
#   mine = mine

#   col = 10
#   row = 10
#   mine = 10

#   limit = col * row

#   mineLocation = generateMines(mine, limit)

# # random generate mines
# def generateMines(mine, limit):
#   mineLocation = []

#   i = 0
#   while i < mine:
#     location = randint(0, limit)
#     if not (location in mineLocation):
#       mineLocation.append(location)
#       i += 1

#   mineLocation.sort()
#   mineInsertMap = insertMine(mineLocation)
#   return mineInsertMap

# # According to the mineLocation, generate map
# def insertMine(list):
#   i = 0
#   board = []
#   for i in limit:
#     if i in list:
#       # 9 indicate
#       board.append(9)
#     else:
#       board.append(0)
#   return board

# # Adding 1 to the mine surroundings
# def plus(list):
#   for i in range(0, len(list)):
#     if list[i] == 9:
#       # add 1 to up and down
#       if (i-col) >= 0:
#         if list[i-col] != 9:
#           list[i-col] += 1
#       if (i + col) <= len(list):
#         if list[i+col] != 9:
#           list[i+col] += 1
#       # check left
#       if (i % col) > 0:
#         if (i-1) >= 0:
#           if list[i-1] != 9:
#             list[i-1] += 1
#         if (i-col-1) >= 0:
#           if list[i-col-1] != 9:
#             list[i-col-1] += 1
#         if (i+col-1) <= len(list):
#           if list[i+col-1] != 9:
#             list[i+col-1] += 1
#       # check right
#       if (i % col) != (col - 1):
#         if (i + 1) <= len(list):
#           if list[i+1] != 9:
#             list[i+1] += 1
#         if (i-col+1) >= 0:
#           if list[i-col+1] != 9:
#             list[i-col+1] += 1
#         if (i+col+1) <= len(list):
#           if list[i+col+1] != 9:
#             list[i+col+1] += 1
