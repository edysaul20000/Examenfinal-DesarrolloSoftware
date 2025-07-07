import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_producto():
    response = client.post("/productos", params={"nombre": "Laptop", "precio": 1000.00})
    assert response.status_code == 200
    assert response.json()["nombre"] == "Laptop"
    assert response.json()["price"] == 1000.00

def test_obtener_producto():
    res = client.post("/productos", params={"nombre": "Smartphone", "precio": 500.00})
    producto_id = res.json()["id"]
    response = client.get(f"/productos/{producto_id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Smartphone"

def test_actualizar_producto():
    res = client.post("/productos", params={"nombre": "Tablet", "price": 300.00})
    producto_id = res.json()["id"]
    response = client.put(f"/productos/{producto_id}", params={"nombre": "Tablet", "precio": 400.00})
    assert response.status_code == 200
    assert response.json()["nombre"] == "Tablet"
    assert response.json()["precio"] == 400.00