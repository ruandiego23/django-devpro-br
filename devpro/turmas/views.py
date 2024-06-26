from django.shortcuts import render

from devpro.modulos import facade


# Create your views here.

def indice(request):
    # ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'turmas/turma.html')
