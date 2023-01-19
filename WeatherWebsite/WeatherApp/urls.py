from django.urls import path
from . import views

#This file needs to be added to the main project.
#In in urls.py inside main project.
urlpatterns = [
    path('', views.index, name='index')
]