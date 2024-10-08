from django.shortcuts import render
# importamos HttpRespose
from django.http import HttpResponse

# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo a traves de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicacion web</h1><br><p>Esta es una prueba de parrafo</p>")

# Crear vista principal
def inicio(request):
    return render(request, 'base.html')