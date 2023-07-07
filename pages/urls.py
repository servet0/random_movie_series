from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie', views.index, name='index'),
    path('series',views.index2, name='index2'),
    path('random_movie', views.random_movie, name='random_movie'),
    path('random_series', views.random_series, name='random_series'),
]