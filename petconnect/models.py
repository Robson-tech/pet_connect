from django.db import models

# Create your models here.

class Loja(models.Model):
    name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_image', blank=True, default='pet_image/default.png')

    def __str__(self):
        return self.name

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    is_dono = models.BooleanField(default=False)
    image = models.ImageField(upload_to='usuario_image', blank=True, default='usuario_image/default.png')

    def __str__(self):
        return self.name

class Agendamento(models.Model):
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    id_animal = models.ForeignKey(Animais, on_delete=models.CASCADE)
    data_hora_agendamento = models.DateTimeField()
    data_hora_consulta = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    desc_problema = models.CharField(max_length=500)

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    preco = models.FloatField()
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    id_promocao = models.ForeignKey(Promocoes, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Animais(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField()
    id_dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='animais_image', blank=True, default='animais_image/default.png')

    def __str__(self):
        return self.name

class Promocoes(models.Model):
    cod = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    duracao = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    porcentagem = models.FloatField()

    def __str__(self):
        return self.cod
    
