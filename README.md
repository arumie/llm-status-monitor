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
or 

```bash
uvicorn llmstatusmonitor.main:api --reload
```

## Endpoints

```
GET /health
```