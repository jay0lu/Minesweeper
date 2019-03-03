from random import randint

def generateMap(col, row, mine):
  limit = col * row
  mineLocation = generateMines(mine, limit)
  fullMap = plus(mineLocation, col)
  mapObj = {
    'mineMap': mineLocation,
    'fullMap': fullMap
  }
  return mapObj

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
  mineInsertMap = insertMine(mineLocation, limit)
  return mineInsertMap

# According to the mineLocation, generate map
def insertMine(list, limit):
  i = 0
  board = []
  for i in range(limit):
    if i in list:
      # 9 indicate
      board.append(9)
    else:
      board.append(0)
  return board

# Adding 1 to the mine surroundings
def plus(list, col):
  for i in range(0, len(list)):
    if list[i] == 9:
      # add 1 to up and down
      if (i-col) >= 0:
        if list[i-col] != 9:
          list[i-col] += 1
      if (i + col) < len(list):
        if list[i+col] != 9:
          list[i+col] += 1
      # check left
      if (i % col) > 0:
        if (i-1) >= 0:
          if list[i-1] != 9:
            list[i-1] += 1
        if (i-col-1) >= 0:
          if list[i-col-1] != 9:
            list[i-col-1] += 1
        if (i+col-1) < len(list):
          if list[i+col-1] != 9:
            list[i+col-1] += 1
      # check right
      if (i % col) != (col - 1):
        if (i + 1) < len(list):
          if list[i+1] != 9:
            list[i+1] += 1
        if (i-col+1) >= 0:
          if list[i-col+1] != 9:
            list[i-col+1] += 1
        if (i+col+1) < len(list):
          if list[i+col+1] != 9:
            list[i+col+1] += 1
  return list