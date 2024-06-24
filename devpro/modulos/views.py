from django.shortcuts import render
from devpro.modulos import facade


# Create your views here.

def modulo(request, slug):
    modulo = facade.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})