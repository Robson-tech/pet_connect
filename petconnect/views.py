from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from .models import Usuario, Animais, Servico, Agendamento


def logar(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return render(request, 'petconnect/index.html')
        else:
            context = {'error': 'Email não cadastrado'}
            return render(request, 'petconnect/login.html', context)
    return render(request, 'petconnect/login.html')


def deslogar(request):
    logout(request)
    return redirect('petconnect:index')


def cadastro(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['nome']
        last_name = request.POST['sobrenome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if senha1 == senha2:
            if Usuario.objects.filter(email=email).exists():
                context['error'] = 'Email já cadastrado'
            else:
                user = Usuario.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, cpf=cpf, telefone=telefone, password=senha1)
                user.save()
                return render(request, 'petconnect/index.html')
        else:
            context['error'] = 'Senhas não conferem'
    return render(request, 'petconnect/cadastro.html', context)


@login_required(login_url='petconnect:login')
def perfil_usuario(request):
    return render(request, 'petconnect/perfil_usuario.html')


@login_required(login_url='petconnect:login')
def cadastro_animal(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        especie = request.POST['especie']
        raca = request.POST['raca']
        sexo = request.POST['sexo']
        animal = Animais.objects.create(
            dono=request.user, nome=nome, idade=idade, especie=especie, raca=raca, sexo=sexo)
        animal.save()
        return redirect('petconnect:perfil_usuario')
    return render(request, 'petconnect/cadastro_animal.html')


@login_required(login_url='petconnect:login')
def consultas_agendadas(request):
    context = {}
    agendamentos = Agendamento.objects.filter(
        usuario=request.user, status=False)
    context['agendamentos'] = agendamentos
    return render(request, 'petconnect/agendamento/agendadas.html', context)


@login_required(login_url='petconnect:login')
def consultas_anteriores(request):
    context = {}
    agendamentos = Agendamento.objects.filter(
        usuario=request.user, status=True)
    context['agendamentos'] = agendamentos
    return render(request, 'petconnect/agendamento/anteriores.html', context)


@login_required(login_url='petconnect:login')
def consultas_pendentes(request):
    return render(request, 'petconnect/agendamento/pendentes.html')


@login_required(login_url='petconnect:login')
def agendar_consulta(request):
    context = {}
    if request.method == 'POST':
        servico_id = request.POST.get('servico', None)
        animal_id = request.POST.get('animal', None)
        data_consulta = request.POST.get('datahorario', None)
        servico = Servico.objects.get(id=servico_id)
        animal = Animais.objects.get(id=animal_id)
        if animal and servico and data_consulta:
            Agendamento.objects.create(
                usuario=request.user, servico=servico, animal=animal, data_consulta=data_consulta)
        return redirect('petconnect:consultas_agendadas')
    else:
        servicos = Servico.objects.all()
        animais = Animais.objects.filter(dono=request.user)
        context['servicos'] = servicos
        context['animais'] = animais
        return render(request, 'petconnect/agendamento/agendar.html', context)


@login_required(login_url='petconnect:login')
def animais_cadastrados(request):
    animais = Animais.objects.filter(dono=request.user)
    context = {'animais': animais}
    return render(request, 'petconnect/animais_cadastrados.html', context)


def servicos(request):
    servicos = Servico.objects.all()
    context = {'servicos': servicos}
    return render(request, 'petconnect/servicos.html', context)
