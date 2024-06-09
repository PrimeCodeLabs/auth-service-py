import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.mark.usefixtures("setup_db")
def test_login_success():
    response = client.post("/token", data={"username": "admin", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.usefixtures("setup_db")
def test_login_failure():
    response = client.post("/token", data={"username": "admin", "password": "wrong_password"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

@pytest.mark.usefixtures("setup_db")
def test_get_user_me():
    response = client.post("/token", data={"username": "admin", "password": "password"})
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"username": "admin", "password": "password"}
