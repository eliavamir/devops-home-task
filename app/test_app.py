import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, DevOps!"


def test_echo_route_success(client):
    payload = {"message": "DevOps test", "status": "ok"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 200
    assert response.get_json() == payload


def test_echo_route_empty(client):
    response = client.post('/echo')
    assert response.status_code == 400