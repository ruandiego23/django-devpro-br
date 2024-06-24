import pytest
from django.urls import reverse
from model_bakery import baker

from devpro.django_assertions import assert_contains
from devpro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo, db)


@pytest.fixture
def aulas(modulo):
    return baker.make(Aula, 3, modulo=modulo)


@pytest.fixture
def response(client, modulo, aulas):
    return client.get(reverse('modulos:modulo', kwargs={'slug': modulo.slug}))


def test_titulo_modulo(response, modulo):
    assert_contains(response, modulo.titulo)


def test_publico_modulo(response, modulo):
    assert_contains(response, modulo.publico)


def test_descricao_modulo(response, modulo):
    assert_contains(response, modulo.descricao)


def test_titulo_de_aulas(response, aulas):
    for aula in aulas:
        assert_contains(response, aula.titulo)


def test_link_de_aulas(response, aulas):
    for aula in aulas:
        assert_contains(response, aula.get_absolute_url())
