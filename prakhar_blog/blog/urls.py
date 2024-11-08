from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/', views.cv, name='cv'),
    path('physics/', views.physics, name='physics'),
    path('algorithms/', views.algorithms, name='algorithms'),
    path('technology/', views.technology, name='technology'),
    path('connect/', views.connect, name='connect'),
]