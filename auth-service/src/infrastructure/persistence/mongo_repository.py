from pymongo import MongoClient
from src.domain.models import User

class MongoRepository:
    def __init__(self):
        client = MongoClient("mongodb://mongodb:27017")
        self.db = client.auth_db
        self.collection = self.db.users

    def get_user(self, username: str):
        user_data = self.collection.find_one({"username": username})
        if user_data:
            return User(username=user_data["username"], password=user_data["password"])
        return None

    def create_user(self, user: User):
        self.collection.insert_one(user.dict())
