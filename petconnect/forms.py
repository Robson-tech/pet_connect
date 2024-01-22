from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'cpf', 'telefone')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'cpf', 'telefone')