from . import app
from fastapi.testclient import TestClient

client = TestClient(app=app)

def test_region_format():
    response = client.get('/region/asia')
    res = response.json()

    assert response.status_code == 200
    assert type(res) == list
    assert type(res[0]) == dict

def test_regions_countries():
    response = client.get('/region/americas')
    res = response.json()

    assert response.status_code == 200
    assert type(res[0]['datetimes'][0]['summary']) == dict
    assert type(res[0]['datetimes'][0]['summary']['date']) == str
    assert type(res[0]['datetimes'][0]['summary']['time']) == str
    assert type(res[0]['datetimes'][0]['timezone']) == str
    assert type(res[0]['datetimes'][0]['datetime']) == str
    assert type(res[0]['country']) == str
    assert type(res[0]['flag']) == str

def test_region_asia():
    response = client.get('/region/asia')
    res = response.json()

    assert response.status_code == 200

def test_region_americas():
    response = client.get('/region/asia')
    res = response.json()

    assert response.status_code == 200

def test_region_europe():
    response = client.get('/region/asia')
    res = response.json()

    assert response.status_code == 200

def test_region_oceania():
    response = client.get('/region/asia')
    res = response.json()

    assert response.status_code == 200

def test_region_africa():
    response = client.get('/region/asia')
    res = response.json()

    assert response.status_code == 200