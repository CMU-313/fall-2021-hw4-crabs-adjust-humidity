import pytest
from apps import app

@pytest.fixture
def client():
    return app.app.test_client()

def test_predict_api(client):
    r = client.get("/predict?age=18&health=5&absences=2")
    assert r.status_code == 200
    assert str(r.json) == '1'