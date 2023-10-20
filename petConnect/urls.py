from django.urls import path

from . import views

app_name = 'petConnect'
urlpatterns = [
    path('', views.inicial, name="home"),

]
