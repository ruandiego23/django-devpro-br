import pytest
from django.test import Client
from django.urls import reverse
from model_bakery import baker

from devpro.django_assertions import assert_contains
from devpro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 3)


@pytest.fixture
def resp(client: Client, modulos):
    return client.get(reverse('base:home'))


def test_titulos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_links_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())
