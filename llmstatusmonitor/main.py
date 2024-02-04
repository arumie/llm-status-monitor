import os
import time
from typing import Any, Callable

from fastapi import FastAPI, Request

from llmstatusmonitor import __project_id__, __version__
from llmstatusmonitor.routers import health, hello, statusmonitor

os.environ["TZ"] = "UTC"

#
#   create the api
#
api = FastAPI(title=f"LLM Status Monitor: {__project_id__}", version=__version__)


#
#   middleware
#
@api.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable) -> Any:
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


#
#   routers
#
api.include_router(health.router)
api.include_router(statusmonitor.router)
api.include_router(hello.router)