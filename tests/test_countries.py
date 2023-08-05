from . import client

def test_timezone():
    response = client.get('/country/united states')
    res = response.json()

    assert response.status_code == 200
    assert type(res['datetimes'][0]['summary']) == dict
    assert type(res['datetimes'][0]['summary']['date']) == str
    assert type(res['datetimes'][0]['summary']['time']) == str
    assert type(res['datetimes'][0]['timezone']) == str
    assert type(res['datetimes'][0]['datetime']) == str

def test_country_with_fullname():
    response = client.get('/country/united states')
    res = response.json()

    assert response.status_code == 200
    assert type(res['datetimes']) == list
    assert type(res['country']) == str

def test_country_with_alpha2():
    response = client.get('/country/us')
    res = response.json()

    assert response.status_code == 200
    assert type(res['datetimes']) == list
    assert type(res['country']) == str

def test_country_with_alpha3():
    response = client.get('/country/usa')
    res = response.json()

    assert response.status_code == 200
    assert type(res['datetimes']) == list
    assert type(res['country']) == str

def test_country_noflag():
    response = client.get('/country/us?emoji=0')
    res = response.json()

    assert response.status_code == 200
    assert 'flag' not in res.keys()