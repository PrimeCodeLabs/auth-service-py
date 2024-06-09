from pymongo import MongoClient
from src.infrastructure.security.jwt import get_password_hash

# Connect to MongoDB
client = MongoClient('mongodb://mongodb:27017/')
db = client['auth_db']

# Drop the users collection if it exists
db.users.drop()

# Insert an admin user
admin_user = {
    "username": "admin",
    "password": get_password_hash("password")  # Hash the password
}

db.users.insert_one(admin_user)

print("Admin user seeded.")
