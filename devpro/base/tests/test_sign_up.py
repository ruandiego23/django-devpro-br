import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:sign_up'))


def test_sign_up_status_code(resp):
    assert resp.status_code == 200
