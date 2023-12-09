from django.shortcuts import render


def index(request):
    return render(request, 'petconnect/index.html')


def contato(request):
    return render(request, 'petconnect/contato.html')


def login(request):
    return render(request, 'petconnect/login.html')


def sobre(request):
    return render(request, 'petconnect/sobre.html')