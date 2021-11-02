import pytest
from apps import app

@pytest.fixture
def client():
    return app.app.test_client()

# test basic functionality 
# When a valid query is given, the result will be successfully returned with expected value.
def test_predict_api(client):
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1")
    assert r.status_code == 200     #correctly returns
    assert str(r.json) == '0'       #check if the result is correct
    r = client.get("/predict?Medu=1&failures=3&schoolsup=0&Dalc=1&Walc=1")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=2&failures=4&schoolsup=0&Dalc=1&Walc=1")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&failures=4&schoolsup=0&Dalc=1&Walc=1")
    assert r.status_code == 200
    assert str(r.json) == '0'

# test for accepting and extracting additional arguments
# When additional unnecessary arguments are given, they will be ignored.
# An error will be thrown when a necessary argument is omitted.
def test_additional_arg(client):
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1&sex=F&age=70")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1&sex=F&age=-14")
    assert r.status_code == 200
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&schoolsup=1&Dalc=1&Walc=1")
    assert r.status_code == 400     # missing arguments will result in Bad Request error with code 400

# test for error input type (string inputs)
# Error will be thrown in the input is not a valid input.
def test_str_type(client):
    r = client.get("/predict?Medu=4&failures=0&schoolsup=1&Dalc=1&Walc=1&sex=F&age=-14")
    assert r.status_code == 200     #A string input, which can be parsed to an integer will be normal
    assert str(r.json) == '0'
    r = client.get("/predict?Medu=4&failures=0&schoolsup=true&Dalc=1&Walc=1&sex=F&age=70")
    assert r.status_code == 400     #A string input, which can't be parsed to an integer will have a response with code 400 (Bad Request)

# test for out of bound input type
# Each input should be checked to see if the value given is a valid input based on the data.
# An error should be thrown in the input values are not valid.
def test_oof(client):
    r = client.get("/predict?Medu=6&failures=0&schoolsup=true&Dalc=1&Walc=1&sex=F&age=70")
    assert r.status_code == 400     #out of bound input will have a response with code 400 (Bad Request)
    r = client.get("/predict?Medu=5&failures=0&schoolsup=true&Dalc=-1&Walc=1&sex=F&age=70")
    assert r.status_code == 400     #out of bound input will have a response with code 400 (Bad Request)
