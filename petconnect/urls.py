from django.urls import path
from . import views


app_name = 'petconnect'
urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('sobre/', views.sobre, name='sobre'),
]
