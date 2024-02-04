from datetime import datetime
from fastapi import APIRouter

from llmstatusmonitor import __version__
from llmstatusmonitor.schemas.health import HealthOutput


router = APIRouter()


@router.get("/health", response_model=HealthOutput, tags=["health"], name="Health Check")
def healthcheck() -> HealthOutput:
    message = "running"
    return HealthOutput(
        message=message,
        version=__version__,
        time=datetime.now(),
    )