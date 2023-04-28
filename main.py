from fastapi import FastAPI
from db import models
from db.database import engine
from routers import address_handler
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(address_handler.router)


@app.get('/')
async def home():
    return {"message": "Address book API"}


models.Base.metadata.create_all(engine)
