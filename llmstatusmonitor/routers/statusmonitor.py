

from fastapi import APIRouter
from pydantic import UUID4

from llmstatusmonitor.schemas.statusmonitor import StatusMonitorOutput
from llmstatusmonitor.services.statusmonitor import StatusMonitorService


router = APIRouter()
statusMonitorService = StatusMonitorService()


@router.get("/status-monitor/{statusMonitorId}", response_model=StatusMonitorOutput, tags=["hello"])
def getHello(statusMonitorId: UUID4) -> StatusMonitorOutput:
    return statusMonitorService.get(statusMonitorId)