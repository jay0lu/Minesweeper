from django.urls import path
from . import views

urlpatterns = [
    path('api/map/', views.MapCreate.as_view() ),
]