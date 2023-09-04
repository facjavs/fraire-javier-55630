from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Oleo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits = 10, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    imagenOleo = models.ImageField(upload_to='imagenes/', null=True, blank=False)

class Acuarela(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits = 10, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    imagenAcuarela = models.ImageField(upload_to='imagenes/', null=True, blank=False)

class Carboncillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits = 10, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    imagenCarboncillo = models.ImageField(upload_to='imagenes/', null=True, blank=False)
    





class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"



