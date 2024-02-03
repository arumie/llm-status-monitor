from datetime import datetime
from fastapi import APIRouter

from llmstatusmonitor import __version__
from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.health import HealthcheckResponse


router = APIRouter()


@router.get("/health", response_model=HealthcheckResponse, tags=["health"])
def healthcheck() -> HealthcheckResponse:
    message = "running"
    logger.info(message)
    return HealthcheckResponse(
        message=message,
        version=__version__,
        time=datetime.now(),
    )