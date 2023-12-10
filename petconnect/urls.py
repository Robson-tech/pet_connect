from django.urls import path
from . import views


app_name = 'petconnect'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
]
