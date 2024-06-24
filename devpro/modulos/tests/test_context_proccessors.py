import pytest
from model_bakery import baker

from devpro.modulos import facade
from devpro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 3)


def test_lista_de_modulos(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.criado_em))[::-1] == facade.listar_modulos_ordenados()
