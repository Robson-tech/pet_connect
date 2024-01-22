from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=False, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    is_dono = models.BooleanField(default=False)
    image = models.ImageField(upload_to='usuario_image', default='usuario_image/default.png', blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=20, null=True, blank=True)
    biografia = models.TextField(max_length=500, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf', 'telefone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Animais(models.Model):
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=100, default='Desconhecido')
    raca = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100, default='Desconhecido')
    image = models.ImageField(upload_to='animais_image', blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_image', blank=True, default='pet_image/default.png')

    def __str__(self):
        return self.nome
    
    
class Promocoes(models.Model):
    cod = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    duracao = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    porcentagem = models.FloatField()

    def __str__(self):
        return self.cod


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    preco = models.FloatField()
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    id_animal = models.ForeignKey(Animais, on_delete=models.CASCADE)
    data_hora_agendamento = models.DateTimeField(auto_now_add=True)
    data_hora_consulta = models.DateTimeField()
    status = models.BooleanField(default=False)
    desc_problema = models.CharField(max_length=500)

    def __str__(self):
        return self.id_loja