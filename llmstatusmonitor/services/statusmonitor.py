from datetime import datetime
from typing import Any, Optional
from pydantic import UUID4, Json

from llmstatusmonitor.daos.statusmonitor import StatusMonitorDAO
from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.statusmonitor import Status, StatusMonitorCreate, StatusMonitorOutput, StatusMonitorUpdate, Type


dao = StatusMonitorDAO()

class StatusMonitorService:
    def create(self, type: Type) -> UUID4:        
        statusMonitor = dao.create(
            StatusMonitorCreate(type=type))
        return statusMonitor.id;

    def get(self, id: UUID4) -> StatusMonitorOutput:
        status_monitor = dao.get(id)

        return StatusMonitorOutput(
            id=str(status_monitor.id),
            type=status_monitor.type.name,
            status=status_monitor.status.name,
            value=str(status_monitor.value) if status_monitor.value is not None else None ,
            time=datetime.now(),
        )
    
    def update(self, id: UUID4, status: Optional[Status], value: Optional[Json[Any]]):
        data = dao.get(id).model_dump()
        if status is not None:
            data["status"] = status.value;
        if value is not None:
            data["value"] = value;
        try:
            status_monitor = dao.update(id, StatusMonitorUpdate(**data))
            return status_monitor
        except Exception as e:
            logger.error(e)
        