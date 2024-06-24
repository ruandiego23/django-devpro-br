from typing import List

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
    return Aula.objects.get(slug=slug)
