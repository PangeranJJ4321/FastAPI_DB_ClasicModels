from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routes.routes import setup_routes 
from middleware.middleware import RequestLoggingMiddleware
from database.base import engine, Base
from database.session import get_db
import uvicorn
import logging

# Create database tables
get_db()
Base.metadata.create_all(bind=engine)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ClassicModels API",
    description="API for ClassicModels database",
    version="1.0.0",
)

# Add middleware
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(setup_routes(), prefix="/api/v1")

# Error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to ClassicModels API",
        "docs": "/docs",
        "redoc": "/redoc",
    }

# Run application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)