from datetime import datetime

from pydantic import BaseModel
from pydantic.types import StrictStr


class HealthResponse(BaseModel):
    message: StrictStr
    version: StrictStr
    time: datetime