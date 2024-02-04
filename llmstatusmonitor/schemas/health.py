from datetime import datetime

from pydantic import BaseModel
from pydantic.types import StrictStr


class HealthOutput(BaseModel):
    message: StrictStr
    version: StrictStr
    time: datetime