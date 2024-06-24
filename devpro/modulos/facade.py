from typing import List

from devpro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Uma lista com módulos ordenados pela data de sua criação.
    """
    return list(Modulo.objects.order_by('criado_em').all())


def encontrar_modulo(slug: str) -> Modulo:
    """
    Encontrar o módulo respectivo ao seu slug
    """
    return Modulo.objects.get(slug=slug)
