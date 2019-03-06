from map.models import Map
from map.serializers import MapSerializer
from rest_framework import generics
from django.http import JsonResponse
import json
from .mineMap import generateMap
import random
import string

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

def changeMap(request, move):
  if request.method == "POST":
    data = json.loads(request.body.decode('utf-8'))
    index = move
    try:
      searchResult = Map.objects.get(uid=uid)
    except:
      print('error')

    map = searchResult.map
    uid = searchResult.uid
    if map[move] == 9:
      return JsonResponse({
        'uid': uid
        'isMine': true
      })
    else:
      currentMap[move] = map[move]
      mapModel = Map(uid=uid, mineMap=map, currentMap=currentMap)
      mapModel.save()
      return JsonResponse({
        'uid': uid
        'map': currentMap
      })

    return JsonResponse({})

def searchGame(request, uid):
  try:
    searchResult = Map.objects.get(uid=uid)
  except:
    print('error')
  return JsonResponse({
    'uid': searchResult.uid,
    'map': searchResult.currentMap
  })
