from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.application.services.auth_service import AuthService
from src.infrastructure.persistence.mongo_repository import MongoRepository
from src.infrastructure.security.jwt import JWTHandler
from src.domain.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_router = APIRouter()
repository = MongoRepository()
jwt_handler = JWTHandler()
auth_service = AuthService(repository, jwt_handler)

limiter = Limiter(key_func=get_remote_address)

@user_router.get("/users/me", response_model=User)
@limiter.limit("5/minute")
async def read_users_me(request: Request, token: str = Depends(oauth2_scheme)):
    username = jwt_handler.verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = repository.get_user(username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
