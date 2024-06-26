import pytest
from django.urls import reverse
from model_bakery import baker

from devpro.django_assertions import assert_contains, assert_not_contains
from devpro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client_with_user_logged, aula):
    return client_with_user_logged.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))


def test_status_code(resp):
    assert resp.status_code == 200


def test_user_name(resp, user_logged):
    assert_contains(resp, user_logged.first_name)


def test_aula_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_login_unavailable(resp, user_logged):
    assert_not_contains(resp, 'Entrar')


@pytest.fixture
def resp_user_not_logged(client, aula):
    return client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))


def test_status_code_user_not_logged(resp_user_not_logged, aula):
    assert resp_user_not_logged.status_code == 302
    assert resp_user_not_logged.url.startswith(reverse('login'))
