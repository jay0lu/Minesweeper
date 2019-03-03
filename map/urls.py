from django.urls import path
from . import views

urlpatterns = [
    path('api/map/', views.MapCreate.as_view() ),
    path('newGame/', views.createMap),
    path('game/(?P<uid>.*)/$', views.searchGame),
    path('moves/', views.changeMap)
]