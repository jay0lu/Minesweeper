from map.models import Map
from map.serializers import MapSerializer
from rest_framework import generics

class MapCreate(generics.ListCreateAPIView):
  queryset = Map.objects.all()
  serializer_class = MapSerializer