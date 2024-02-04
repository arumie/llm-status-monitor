# LLM Status Monitor

## Description

Project to allow invocation of LLMs with a status monitor using FastApi and Google Firestore

Purpose is for use in serverless functions with low timeout (Ex. a free project using Vercel and NextJS)

## Setup

Python version

```
3.11.6
```

Install dependencies

```bash
pip install -r requirement.txt
```

## Run

```bash
./scripts/run.sh
```

or when wanting to use a Mock Firestore

```bash
./scripts/runMock.sh
```

## Endpoints

```
GET /health -> HealthOutput
POST /hello -> StatusMonitorOutput
GET /status-monitor/{id} -> StatusMonitorOutput
```

Swagger is available at http://localhost:8000/docs
