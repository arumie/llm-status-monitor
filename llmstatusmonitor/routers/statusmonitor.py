

from fastapi import APIRouter, Security
from pydantic import UUID4
from llmstatusmonitor.auth import get_api_key

from llmstatusmonitor.schemas.statusmonitor import StatusMonitorOutput
from llmstatusmonitor.services.statusmonitor import StatusMonitorService


router = APIRouter()
statusMonitorService = StatusMonitorService()


@router.get("/status-monitors/{statusMonitorId}", response_model=StatusMonitorOutput, tags=["status-monitor"], name="Get Status Monitor")
def getHello(statusMonitorId: UUID4, api_key = Security(get_api_key)) -> StatusMonitorOutput:
    return statusMonitorService.get(statusMonitorId)