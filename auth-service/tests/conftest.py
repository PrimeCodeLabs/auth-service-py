from fastapi.testclient import TestClient
import pytest
from pymongo import MongoClient
from src.main import app

# Ensure the src directory is in the sys.path

@pytest.fixture(scope='module')
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope='module')
def setup_db():
    client = MongoClient("mongodb://mongodb:27017")
    db = client.auth_db
    users_collection = db.users
    test_user = {"username": "admin", "password": "password"}
    users_collection.insert_one(test_user)
    yield
    users_collection.delete_many({})