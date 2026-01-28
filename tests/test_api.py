from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "CI/CD FastAPI is working"}


def test_add():
    response = client.get("/add?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_even_true():
    response = client.get("/even/10")
    assert response.status_code == 200
    assert response.json() == {"is_even": True}


def test_even_false():
    response = client.get("/even/7")
    assert response.status_code == 200
    assert response.json() == {"is_even": False}
