from fastapi import FastAPI
from src.controllers.api.auth_router import auth_router
from src.controllers.api.user_router import user_router
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()
# Initialize rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="redis://redis:6379"
)


# Add rate limiting middleware
app.add_middleware(SlowAPIMiddleware)

# Apply rate limiter to the whole application
app.state.limiter = limiter

app.include_router(auth_router)
app.include_router(user_router)
