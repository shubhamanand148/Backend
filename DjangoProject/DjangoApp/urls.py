from django.urls import path
from . import views

urlpatterns = [

    #This is the default/Home page of the website. It gets the look from template -> index.html
    path('', views.index, name='index'),


    path('count', views.count, name='count')
]