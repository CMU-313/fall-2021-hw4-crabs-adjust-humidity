import pytest
from apps import app

@pytest.fixture
def client():
    return app.app.test_client()

#test basic functionality -- how predicted result match labels
def test_predict_api(client):
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1")
    assert r.status_code == 200     #corectly returns
    assert str(r.json) == '0'       #check if the result is corret
    r = client.get("/predict?Medu=1&failures=3&schoolsup=0&Dalc=1&Walc=1")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=2&failures=4&schoolsup=0&Dalc=1&Walc=1")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&failures=4&schoolsup=0&Dalc=1&Walc=1")
    assert r.status_code == 200
    assert str(r.json) == '0'

#test for accepting and extracting additional arguements
def test_additional_arg(client):
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1&sex=F&age=70")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1&sex=F&age=-14")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&schoolsup=1&Dalc=1&Walc=1")
    assert r.status_code == 400

#test for error input type (string inputs)
def test_str_type(client):
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1&sex=F&age=-14")
    assert r.status_code == 200     #A string input, which can be parsed to an integer will be normal
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&failures=0&schoolsup=true&Dalc=1&Walc=1&sex=F&age=70")
    assert r.status_code == 400     #A string input, which can't be parsed to an integer will have a response with code 400(Bad Request)

#test for out of bound input type
def test_str_type(client):
    r = client.get("/predict?Medu=6&failures=0&schoolsup=true&Dalc=1&Walc=1&sex=F&age=70")
    assert r.status_code == 400     #out of bound input will have a response with code 400(Bad Request)
    r = client.get("/predict?Medu=5&failures=0&schoolsup=true&Dalc=-1&Walc=1&sex=F&age=70")
    assert r.status_code == 400     #out of bound input will have a response with code 400(Bad Request)