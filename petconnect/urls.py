from django.urls import path
from . import views

name = 'petconnect'

urlpatterns = [
    path('', views.index, name='index'),
]
