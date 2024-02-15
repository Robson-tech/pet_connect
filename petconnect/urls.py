from django.views.generic import TemplateView
from django.urls import path
from . import views


app_name = 'petconnect'
urlpatterns = [
    path('', TemplateView.as_view(
        template_name='petconnect/index.html'), name='index'),
    path('contato/', TemplateView.as_view(template_name='petconnect/contato.html'), name='contato'),
    path('sobre/', TemplateView.as_view(template_name='petconnect/sobre.html'), name='sobre'),
    path('perfil_petshop/', TemplateView.as_view(template_name='petconnect/perfil_petshop.html'), name='perfil_petshop'),
    path('avaliacoes/', TemplateView.as_view(template_name='petconnect/avaliacoes.html'), name='avaliacoes'),

    path('login/', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('cadastro_animal/', views.cadastro_animal, name='cadastro_animal'),
    path('consultas/agendadas', views.consultas_agendadas,
         name='consultas_agendadas'),
    path('consultas/anteriores', views.consultas_anteriores,
         name='consultas_anteriores'),
    path('consultas/pendentes', views.consultas_pendentes,
         name='consultas_pendentes'),
    path('agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('servicos/', views.servicos, name='servicos'),
    path('animais_cadastrados/', views.animais_cadastrados, name='animais_cadastrados'),
]
