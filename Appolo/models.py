from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    estiloAprendizaje = models.CharField(max_length=50)
    estiloAprendizaje2 = models.CharField(max_length=50, default="Nuevo")
    resultado = models.IntegerField(default=0)
    temaProgreso = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

