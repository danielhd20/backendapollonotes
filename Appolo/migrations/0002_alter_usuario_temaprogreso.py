# Generated by Django 4.1.4 on 2023-01-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appolo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='TemaProgreso',
            field=models.CharField(max_length=100),
        ),
    ]
