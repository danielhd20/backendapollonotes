# Generated by Django 4.1.4 on 2023-01-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appolo', '0003_rename_temaprogreso_usuario_temaprogreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estiloAprendizaje2',
            field=models.CharField(default='Nuevo', max_length=50),
        ),
    ]
