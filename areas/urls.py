from django.urls import path
from . import views

urlpatterns = [
    path('', views.areas, name='areas'),
]
