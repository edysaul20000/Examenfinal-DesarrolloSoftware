import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_usuario():
    response = client.post("/usuarios", params={"nombre": "Edy"})
    assert response.status_code == 200
    assert response.json()["nombre"] == "Edy"

def test_listar_usuarios():
    client.post("/usuarios", params={"nombre": "Jairo"})
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert any(u["nombre"] == "Jairo" for u in response.json())

def test_eliminar_usuario():
    res = client.post("/usuarios", params={"nombre": "Luffy"})
    usuario_id = res.json()["id"]
    elim_res = client.delete(f"/usuarios/{usuario_id}")
    assert elim_res.status_code == 200
    assert elim_res.json()["mensaje"] == "Usuario eliminado"
