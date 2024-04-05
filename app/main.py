from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from app.router import user

from app.settings import settings

app = FastAPI(title=settings.APP_NAME, description=settings.DESCRIPTION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FASTAPI_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add main routes to the api
app.include_router(user.router)



