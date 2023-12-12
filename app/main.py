from fastapi import FastAPI

from app.core.database.mysql.database import engine
from app.core.models.mysql import models
from app.features.user.presentation.routes.user_routes import user_router

app = FastAPI()
app.include_router(user_router)


@app.on_event('startup')
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {"message": "Hello I'm alive"}
