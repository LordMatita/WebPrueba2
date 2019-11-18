from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(primary_key=True, max_length = 100) 

    tupla_genero = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    genero = models.CharField(
        max_length = 1,
        choices = tupla_genero,
        blank = True,
        default = 'H',
        help_text = 'Género del entrenador',
        )

    def _str_(self):
        return f'{self.nombre}, {self.genero}'

class Pokemon(models.Model):
    tupla_nombre = (
        ('Bulbasaur','Bulbasaur'),
        ('Squirtle', 'Squirtle'),
        ('Charmander', 'Charmander'),
        ('Pikachu', 'Pikachu'),
        ('Chikorita','Chikorita'),
        ('Totodile','Totodile'),
        ('Cyndaquil','Cyndaquil'),
        ('Treecko','Treecko'),
        ('Torchic','Torchic'),
    )

    nombre = models.CharField(
        max_length = 100,
        choices = tupla_nombre,
        blank = True,
        default = 'Bulbasaur',
        help_text = 'Nombre del pokemon',
        ) 
        
    descripcion = models.CharField(max_length = 200)

    tupla_region = (
        ('K', 'Kanto'),
        ('J', 'Johto'),
        ('H', 'Hoenn'),
    )

    region = models.CharField(
        max_length = 1,
        choices = tupla_region,
        blank = True,
        default = 'K',
        help_text = 'Region de procedencia del pokemon',
        )
    
    def _str_(self):
        return f'{self.nombre}, {self.descripcion}, {self.region}'

