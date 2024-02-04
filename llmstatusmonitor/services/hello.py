import asyncio
from typing import Any

from pydantic import UUID4, Json
from llmstatusmonitor.logger import logger

from llmstatusmonitor.schemas.statusmonitor import Status, Type
from llmstatusmonitor.services.statusmonitor import StatusMonitorService


statusMonitorService = StatusMonitorService()


class HelloWorldService:

    async def create(self, str: Json[Any], statusMonitorId: UUID4) -> None:
        logger.info("Stuff initiated...")
        await asyncio.sleep(5)
        logger.info("Done with stuff... Setting status to SUCCESSFUL")
        statusMonitorService.update(
            statusMonitorId, status=Status.SUCCESSFUL, value=str)
