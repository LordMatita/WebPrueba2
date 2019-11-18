from django.contrib import admin

# Register your models here.

from . models import Entrenador, Pokemon

admin.site.register(Entrenador)
admin.site.register(Pokemon)

