from os import name
from django.urls import path

# from SM_DetectorApp import urls
from . import views

urlpatterns = [
    path('mriaction/', views.MriAction, name='MriAction'),
    path('', views.MriHtml, name='MriHtml'),
    path('inlet/', views.Inlet, name='Inlet'),
]