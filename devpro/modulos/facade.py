from typing import List

from django.db.models import Prefetch

from devpro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Uma lista com módulos ordenados pela data de sua criação.
    """
    return list(Modulo.objects.order_by('-criado_em').all())


def encontrar_modulo(slug: str) -> Modulo:
    """
    Encontrar o módulo respectivo ao seu slug.
    """
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulos_ordenados(modulo: Modulo):
    """
    Uma lista de aulas correspondente a um módulo.
    """
    return list(modulo.aula_set.order_by('-criado_em').all())


def encontrar_aula(slug):
    """
    Encontrar aula de acordo com o slug.
    """
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    """
    Todos os módulos e suas respectivas aulas.
    """
    aulas_ordenadas = Aula.objects.order_by('-criado_em')
    return (Modulo.objects.order_by('-criado_em').prefetch_related(
        Prefetch(
            'aula_set', queryset=aulas_ordenadas, to_attr='aulas')
    ).all())
