from map.models import Map
from map.serializers import MapSerializer
from rest_framework import generics
from django.http import JsonResponse
import json
from .mineMap import generateMap
import random
import string
import ast

class MapCreate(generics.ListCreateAPIView):
  queryset = Map.objects.all()
  serializer_class = MapSerializer


def createMap(request):
  uid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
  col = 10
  row = 10
  mines = 30
  mapObject = generateMap(col, row, mines)
  mineMapLocation = mapObject['mineMap']
  fullMapLocation = mapObject['fullMap']
  newCurrentMap = [-1] * col * row

  mapModel = Map(uid=uid, mineMap=fullMapLocation, currentMap=newCurrentMap)
  mapModel.save()
  return JsonResponse({
    'uid': uid,
    'map': newCurrentMap
  })

def changeMap(request):
  if request.method == "POST":
    data = json.loads(request.body.decode('utf-8'))
    searchResult = {}
    uid = data['uid']
    move = data['position']

    try:
      searchResult = Map.objects.get(uid=uid)
    except:
      print('error')

    print(searchResult)
    mapStr = searchResult.mineMap
    currentMapStr = searchResult.currentMap
    map = ast.literal_eval(mapStr)
    currentMap = ast.literal_eval(currentMapStr)

    if map[move] == 9:
      return JsonResponse({
        'uid': uid,
        'map': currentMap,
        'isMine': true
      })
    else:
      currentMap[move] = map[move]
      searchResult.currentMap = currentMap
      searchResult.save()
      return JsonResponse({
        'uid': uid,
        'map': currentMap,
        'isMine': false
      })

def searchGame(request, uid):
  try:
    searchResult = Map.objects.get(uid=uid)
  except:
    print('error')
  return JsonResponse({
    'uid': searchResult.uid,
    'map': searchResult.currentMap
  })
