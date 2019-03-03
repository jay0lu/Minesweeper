from django.urls import path
from . import views

urlpatterns = [
    path('api/map/', views.MapCreate.as_view() ),
    path('newGame/', views.create_map),
    path('newGame/(?P<user_id>.*)/', views.create_map),
    path('moves/', views.change_map)
]