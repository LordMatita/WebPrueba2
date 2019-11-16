from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(primary_key=True, max_length = 100) 
    genero = models.CharField(max_length = 1)

    def _str_(self):
        return f'{self.nombre}, {self.genero}'

class Pokemon(models.Model):
    nombre = models.CharField(max_length = 100) 
    descripcion = models.CharField(max_length = 200)
    region = models.CharField(max_length= 100)

    def _str_(self):
        return f'{self.nombre}, {self.descripcion}, {self.region}'

