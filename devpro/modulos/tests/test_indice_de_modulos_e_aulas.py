import pytest
from django.urls import reverse
from model_bakery import baker

from devpro.django_assertions import assert_contains
from devpro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas_list = []
    for modulo in modulos:
        aulas_list.extend(baker.make(Aula, 2, modulo=modulo))
    return aulas_list


@pytest.fixture
def resp(client, modulos, aulas):
    return client.get(reverse('modulos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_modulo_indice(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_publico_modulo_indice(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_descricao_modulo_indice(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_titulo_aula_indice(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_link_aula_indice(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
