"""Health check endpoints."""

from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", response_model=dict)
async def health_check():
    """Health check endpoint for monitoring and load balancers."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "python-microservice-template",
        "version": "1.0.0",
    }


@router.get("/health/ready", response_model=dict)
async def readiness_check():
    """Readiness probe for Kubernetes."""
    return {"status": "ready"}


@router.get("/health/live", response_model=dict)
async def liveness_check():
    """Liveness probe for Kubernetes."""
    return {"status": "alive"}
