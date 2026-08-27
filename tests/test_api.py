from fastapi.testclient import TestClient

from script.app import app


client = TestClient(app)


def test_inicio():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "Mi Calculadora DevOps está funcionando"
    }

def test_sumar_api():
    response = client.get("/sumar?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"resultado": 8}

def test_restar_api():
    response = client.get("/restar?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"resultado": 2}


def test_multiplicar_api():
    response = client.get("/multiplicar?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"resultado": 15}


def test_dividir_api():
    response = client.get("/dividir?a=10&b=2")

    assert response.status_code == 200
    assert response.json() == {"resultado": 5}