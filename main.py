from fastapi import FastAPI
from routes.routes import setup_routes
from database.base import engine, Base
from models.models import Customer, Employee, Order, OrderDetail, Product, ProductLine, Office, Payment 
from database.session import get_db

app = FastAPI()

get_db()
Base.metadata.create_all(bind=engine)


app.include_router(setup_routes(), prefix="/api/v1")


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to ClassicModels API",
        "docs": "/docs",
        "redoc": "/redoc",
    }

