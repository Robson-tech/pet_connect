# Generated by Django 5.0 on 2023-12-17 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petconnect', '0003_alter_usuario_data_nascimento_alter_usuario_endereco_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animais',
            old_name='id_dono',
            new_name='dono',
        ),
    ]
