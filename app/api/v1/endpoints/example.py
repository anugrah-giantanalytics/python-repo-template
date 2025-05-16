from typing import Dict

from fastapi import APIRouter, HTTPException

from app.core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)


@router.get("/example", response_model=Dict[str, str])
async def example_endpoint() -> Dict[str, str]:
    """
    Example endpoint demonstrating basic structure.
    
    Returns:
        Dict[str, str]: A simple message
    """
    try:
        logger.info("Processing example endpoint request")
        return {"message": "Hello from the example endpoint!"}
    except Exception as e:
        logger.error("Error processing example endpoint request", error=str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        ) 