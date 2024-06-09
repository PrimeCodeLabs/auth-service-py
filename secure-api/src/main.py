from fastapi import FastAPI
from src.controllers.api.secure_router import secure_router

app = FastAPI()

app.include_router(secure_router)
