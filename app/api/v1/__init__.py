from fastapi import APIRouter

from app.api.v1.endpoints import example

# Create API router
router = APIRouter()

# Include routes from endpoints
router.include_router(example.router, prefix="/example", tags=["example"]) 