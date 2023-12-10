from django.urls import path
from . import views


app_name = 'petconnect'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
]
