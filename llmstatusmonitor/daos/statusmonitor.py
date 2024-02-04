from fastapi import HTTPException
from pydantic import UUID4
from llmstatusmonitor.logger import logger
from llmstatusmonitor.schemas.statusmonitor import Status, StatusMonitor, StatusMonitorCreate, StatusMonitorUpdate, Type
from llmstatusmonitor.database import db


class StatusMonitorDAO:
    collection_name = "status-monitor"

    def create(self, create: StatusMonitorCreate) -> StatusMonitor:
        data = create.model_dump()
        id = create.id
        data["id"] = str(id)
        data["status"] = create.status
        data["type"] = create.type
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.set(data)
        return self.get(id)

    def get(self, id: UUID4) -> StatusMonitor:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            return StatusMonitor(**doc_dict)
        else:            
            raise HTTPException(status_code=404, detail=f"Status monitor with id {str(id)} not found")
        

    def update(self, id: UUID4, item_update: StatusMonitorUpdate) -> StatusMonitor:
        data = item_update.model_dump()
        if item_update.value is not None:
            data["value"] = str(item_update.value).replace('\'', '\"')
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID4) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
