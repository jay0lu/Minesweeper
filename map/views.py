from map.models import Map
from map.serializers import MapSerializer
from rest_framework import generics
from django.http import HttpResponse
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
  return HttpResponse({
    uid: uid,
    map: newCurrentMap
  })

def changeMap(request):
  if request.method == "POST":
    data = json.loads(request.body.decode('utf-8'))
    index = data["position"]
    mapObj = Map.objects.all()[0]
    mapObj.mineMap = str(index)
    mapObj.save()
    return HttpResponse({})

def searchGame(request, uid):
  try:
    searchResult = Map.objects.filter(uid=uid).first()
    print(searchResult)
  except:
    print('--')
  return HttpResponse({})
