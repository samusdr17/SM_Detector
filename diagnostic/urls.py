from django.urls import path
from . import views


urlpatterns = [
    path('', views.Diagnostic, name='Diagnostic'),
]