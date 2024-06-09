from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.application.services.auth_service import AuthService
from src.infrastructure.persistence.mongo_repository import MongoRepository
from src.infrastructure.security.jwt import JWTHandler
from src.domain.models import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_router = APIRouter()
repository = MongoRepository()
jwt_handler = JWTHandler()
auth_service = AuthService(repository, jwt_handler)

limiter = Limiter(key_func=get_remote_address)

@auth_router.post("/token", response_model=Token)
@limiter.limit("5/minute")
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
