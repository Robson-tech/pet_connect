from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_image', blank=True)

    def __str__(self):
        return self.name

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    image = models.ImageField(upload_to='usuario_image', blank=True)

    def __str__(self):
        return self.name


    
