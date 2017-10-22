import falcon
from falcon import testing

import pytest
from api.app import api


@pytest.fixture(name="client")
def fixture_client():
    return testing.TestClient(api)


def test_healt_check(client):
    response = client.simulate_get('/_health')
    assert response.status == falcon.HTTP_200
