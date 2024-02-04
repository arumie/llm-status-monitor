from datetime import datetime
from fastapi import APIRouter

from llmstatusmonitor import __version__
from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.health import HealthOutput


router = APIRouter()


@router.get("/health", response_model=HealthOutput, tags=["health"])
def healthcheck() -> HealthOutput:
    message = "running"
    logger.info(message)
    return HealthOutput(
        message=message,
        version=__version__,
        time=datetime.now(),
    )