# Generated by Django 5.0 on 2024-01-22 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petconnect', '0007_alter_agendamento_data_hora_agendamento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='id_promocao',
        ),
    ]
