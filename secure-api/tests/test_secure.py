import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_access_secure_data():
    # Obtain token from auth service first
    auth_response = client.post("http://auth-service:8000/token", data={"username": "admin", "password": "password"})
    token = auth_response.json()["access_token"]
    
    # Access secure endpoint
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/secure-data", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"data": "This is secure data", "user": "admin"}
