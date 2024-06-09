from datetime import datetime, timedelta
from src.domain.models import User
from src.infrastructure.persistence.mongo_repository import MongoRepository
from src.infrastructure.security.jwt import JWTHandler
from passlib.context import CryptContext

class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, repository: MongoRepository, jwt_handler: JWTHandler):
        self.repository = repository
        self.jwt_handler = jwt_handler

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def authenticate_user(self, username: str, password: str):
        user = self.repository.get_user(username)
        if user and self.verify_password(password, user.password):
            return user
        return None

    def create_access_token(self, user: User):
        expires_delta = timedelta(minutes=30)
        access_token = self.jwt_handler.create_token(data={"sub": user.username}, expires_delta=expires_delta)
        return access_token
