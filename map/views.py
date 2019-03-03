from map.models import Map
from map.serializers import MapSerializer
from rest_framework import generics
from django.http import HttpResponse
import json
from .mineMap import generateMap

class MapCreate(generics.ListCreateAPIView):
  queryset = Map.objects.all()
  serializer_class = MapSerializer


def create_map(request, user_id=None):
  if not user_id:
    user_id = "anonymous"
  new_map = Map.objects.get_or_create(uid=user_id)
  mapObject = generateMap(10, 10, 30)
  mineMapLocation = mapObject['mineMap']
  fullMapLocation = mapObject['fullMap']
  print('===')
  print(fullMapLocation)
  print(mineMapLocation)
  return HttpResponse({})

def change_map(request):
  if request.method == "POST":
    data = json.loads(request.body.decode('utf-8'))
    index = data["position"]
    map_obj = Map.objects.all()[0]
    map_obj.mineMap = str(index)
    map_obj.save()
    return HttpResponse({})