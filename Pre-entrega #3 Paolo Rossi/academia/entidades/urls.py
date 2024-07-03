from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', home, name="home"),
    path('comprar/', comprar, name="comprar"),
    path('projects/', projects, name="projects"),
    path('producto/', producto, name="producto"),
    path('admin/', home, name="home"),
    path('', home, name="home"),
]
