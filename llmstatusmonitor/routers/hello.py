
from fastapi import APIRouter, BackgroundTasks
from pydantic import UUID4

from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.statusmonitor import StatusMonitorOutput, Type
from llmstatusmonitor.services.hello_world import HelloWorldService
from llmstatusmonitor.services.statusmonitor import StatusMonitorService


router = APIRouter()
helloWorldService = HelloWorldService()
statusMonitorService = StatusMonitorService()


@router.post("/hello", response_model=StatusMonitorOutput, tags=["hello"])
def createHello(backgroundTasks: BackgroundTasks) -> StatusMonitorOutput:    
    logger.info("Creating new PENDING status monitor")
    statusMonitorId = statusMonitorService.create(Type.HELLO_WORLD)
    backgroundTasks.add_task(helloWorldService.create, '{"value": "world"}', statusMonitorId)
    return statusMonitorService.get(statusMonitorId)