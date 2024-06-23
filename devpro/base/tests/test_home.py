import pytest
from django.test import Client
from django.urls import reverse

from devpro.django_assertions import assert_contains


@pytest.fixture
def response(client: Client):
    return client.get(reverse('base:home'))


def test_home_status_code(response):
    assert response.status_code == 200


def test_titulo_home(response):
    assert_contains(response, '<title>home')


def test_link_home(response):
    assert_contains(response, f'<a class="nav-link active" aria-current="page" href="{reverse("base:home")}">Home</a>')
