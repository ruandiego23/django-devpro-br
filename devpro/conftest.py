"""
Com o arquivo conftest.py, o pytest-django pode acessar esses testes em quaisquer apps
"""
import pytest

from devpro.base.models import User


@pytest.fixture
def user_logged(db):
    """
    Modelo de um usuario
    """
    usuario_modelo = User.objects.create_user(email='<EMAIL>', first_name='John', password='<PASSWORD>')
    usuario_modelo.save()
    return usuario_modelo


@pytest.fixture
def client_with_user_logged(user_logged, client):
    """
    Usuario logado
    """
    client.force_login(user_logged)
    return client
