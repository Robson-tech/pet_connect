from django.urls import path
from . import views


app_name = 'petconnect'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('cadastro_animal/', views.cadastro_animal, name='cadastro_animal'),
    path('consultas/agendadas', views.consultas_agendadas, name='consultas_agendadas'),
    path('consultas/anteriores', views.consultas_anteriores, name='consultas_anteriores'),
    path('consultas/pendentes', views.consultas_pendentes, name='consultas_pendentes'),
    path('agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
]
