import logging
import os
import time


def create_logger() -> logging.Logger:

    green = "\x1b[32;20m"
    reset = "\x1b[0m"
    logging.basicConfig(
        format=(
            f"{green}%(asctime)s{reset}: "
            f"[process=%(process)s] [%(pathname)s: line %(lineno)d] "
            "%(levelname)s: %(message)s"
        ),
        level=os.environ.get("LOGLEVEL", "INFO").upper(),
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    return logger


logger = create_logger()
