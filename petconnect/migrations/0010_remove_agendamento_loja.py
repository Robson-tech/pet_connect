# Generated by Django 5.0 on 2024-01-25 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petconnect', '0009_rename_id_animal_agendamento_animal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='loja',
        ),
    ]