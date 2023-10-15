│#!/bin/bash

echo "Worker Initiated"

echo "Starting WebUI API"

uvicorn main:app --host 0.0.0.0 --port 1118 &

echo "Starting RunPod Handler"
python -u /handler.py
