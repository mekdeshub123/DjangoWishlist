#This file take the assignment from wishlis/urls.py to routing
#  requests for whole sites 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('was_visited', views.place_was_visited, name='place_was_visited')
]
