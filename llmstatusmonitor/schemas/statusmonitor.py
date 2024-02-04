from datetime import datetime
from enum import Enum
from typing import Any, Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field, Json
from pydantic.types import StrictStr


class Status(Enum):
    PENDING = 1
    SUCCESSFUL = 2
    FAILED = 3

class Type(Enum):
    HELLO_WORLD = 1

class StatusMonitorBase(BaseModel):
    id: UUID4
    type: Type
    status: Status
    value: Optional[Any] = None

class StatusMonitorOutput(BaseModel):
    id: UUID4
    type: StrictStr
    status: StrictStr
    value: Optional[Any]
    time: datetime

class StatusMonitorCreate(StatusMonitorBase):
    id: UUID4 = Field(default_factory=uuid4)
    status: Status = Field(default=Status.PENDING)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StatusMonitorUpdate(StatusMonitorBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "An Item",
                "desc": "A very peculiar item.",
            }
        }


class StatusMonitor(StatusMonitorBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True