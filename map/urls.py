from django.urls import path, re_path
from . import views

urlpatterns = [
    path('api/map/', views.MapCreate.as_view() ),
    path('newGame/', views.createMap),
    re_path('game/(?P<uid>.*)/$', views.searchGame),
    re_path('moves/(?P<move>.*)/$', views.changeMap)
]