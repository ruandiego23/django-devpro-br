import pytest
from django.urls import reverse
from model_bakery import baker

from devpro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_with_user_logged(client_with_user_logged, db):
    return client_with_user_logged.get(reverse('base:home'))


def test_button_exit_available(resp_with_user_logged):
    assert_contains(resp_with_user_logged, 'Sair')


def test_user_name_available(resp_with_user_logged, user_logged):
    assert_contains(resp_with_user_logged, user_logged.first_name)


def test_link_exit_available(resp_with_user_logged, user_logged):
    assert_contains(resp_with_user_logged, reverse('logout'))


def test_button_login_unavailable(resp_with_user_logged):
    assert_not_contains(resp_with_user_logged, 'Entrar')


def test_link_of_link_unavailable(resp_with_user_logged):
    assert_not_contains(resp_with_user_logged, reverse('login'))
