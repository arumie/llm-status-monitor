
from fastapi import APIRouter, BackgroundTasks
from pydantic import StrictStr

from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.statusmonitor import StatusMonitorOutput, Type
from llmstatusmonitor.services.hello import HelloWorldService
from llmstatusmonitor.services.statusmonitor import StatusMonitorService


router = APIRouter()
helloWorldService = HelloWorldService()
statusMonitorService = StatusMonitorService()


@router.post("/hello", response_model=StatusMonitorOutput, tags=["hello"], name="Create Hello Resource")
def createHello(value: StrictStr, backgroundTasks: BackgroundTasks) -> StatusMonitorOutput:    
    logger.info("Creating new PENDING status monitor")
    statusMonitorId = statusMonitorService.create(Type.HELLO_WORLD)
    backgroundTasks.add_task(helloWorldService.create, '{"value": "' + value + '"}', statusMonitorId)
    return statusMonitorService.get(statusMonitorId) 