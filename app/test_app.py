import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_echo_route_empty(client):
    response = client.post('/echo')
    assert response.status_code == 415
