from django.shortcuts import render


def index(request):
    return render(request, 'petconnect/index.html')


def login(request):
    return render(request, 'petconnect/login.html')


def cadastro(request):
    return render(request, 'petconnect/cadastro.html')


def contato(request):
    return render(request, 'petconnect/contato.html')


def sobre(request):
    return render(request, 'petconnect/sobre.html')