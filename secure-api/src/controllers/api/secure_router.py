from fastapi import APIRouter, Depends
from src.security.verify_token import verify_token

secure_router = APIRouter()

@secure_router.get("/secure-data")
async def read_secure_data(username: str = Depends(verify_token)):
    return {"data": "This is secure data", "user": username}
