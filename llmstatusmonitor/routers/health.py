from datetime import datetime
from fastapi import APIRouter

from llmstatusmonitor import __version__
from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.health import HealthResponse


router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["health"])
def healthcheck() -> HealthResponse:
    message = "running"
    logger.info(message)
    return HealthResponse(
        message=message,
        version=__version__,
        time=datetime.now(),
    )