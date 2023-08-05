from . import app
from fastapi.testclient import TestClient

client = TestClient(app=app)

def test_subregion_region():
    response = client.get('/subregions/europe')
    res = response.json()

    assert response.status_code == 200
    assert res['region'] == 'europe'

def test_subregions_names():
    response = client.get('/subregions/asia')
    res = response.json()

    assert response.status_code == 200
    assert type(res['subregions names']) == list
    assert type(res['subregions names'][0]) == str

def test_subregions():
    response = client.get('/subregions/americas')
    res = response.json()

    assert response.status_code == 200
    assert type(res['subregions']) == list
    assert type(res['subregions'][0][res['subregions names'][0]]) == list

def test_subregions_countries():
    response = client.get('/subregions/europe')
    res = response.json()
    country = res['subregions'][0][res['subregions names'][0]][0] 

    assert response.status_code == 200
    assert type(country['datetimes'][0]['summary']) == dict
    assert type(country['datetimes'][0]['summary']['date']) == str
    assert type(country['datetimes'][0]['summary']['time']) == str
    assert type(country['datetimes'][0]['timezone']) == str
    assert type(country['datetimes'][0]['datetime']) == str
    assert type(country['country']) == str
    assert type(country['flag']) == str