#!/bin/sh -e

ENV="mock" uvicorn llmstatusmonitor.main:api --reload