import pytest
from aceest import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as c:
        yield c

def test_health(client):
    r = client.get('/health')
    assert r.status_code == 200
    assert r.get_json()['status'] == 'ok'

def test_create_and_get_gym(client):
    r = client.post('/gyms', json={'name': 'Downtown Gym'})
    assert r.status_code == 201
    gid = r.get_json()['id']
    r2 = client.get(f'/gyms/{gid}')
    assert r2.status_code == 200

def test_add_member(client):
    r = client.post('/gyms', json={'name': 'Corner Gym'})
    gid = r.get_json()['id']
    r2 = client.post(f'/gyms/{gid}/members', json={'member': 'Alice'})
    assert r2.status_code == 200
    assert 'Alice' in r2.get_json()['members']
