from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from devpro.modulos import facade


# Create your views here.

def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.htm', ctx)


def modulo_aulas(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


@login_required(login_url='login')
def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
