from django.shortcuts import render
from .models import Entrenador, Pokemon

# Create your views here.

def index(request):
    num_pokemon=Pokemon.objects.all().count()
    num_entrenador= Entrenador.objects.all().count()

    num_pokemon_kanto=Pokemon.objects.filter(region__exact='K').count()
    num_pokemon_johto=Pokemon.objects.filter(region__exact='J').count()
    num_pokemon_hoenn=Pokemon.objects.filter(region__exact='H').count()

    return render(
        request,
        'index.html' ,
        context={'num_pokemon':num_pokemon,'num_entrenador':num_entrenador,'num_pokemon_kanto':num_pokemon_kanto,'num_pokemon_johto':num_pokemon_johto,'num_pokemon_hoenn':num_pokemon_hoenn},
    )