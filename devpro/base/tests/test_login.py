import pytest
from django.urls import reverse

from devpro.django_assertions import assert_contains, assert_not_contains


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
