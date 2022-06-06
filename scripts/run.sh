#!/bin/bash
echo "[SERVER] Starting ..."

echo "[SERVER] Activate the virtual environment"
cd ..
./venv/Scripts/activate

cd api
set FLASK_APP=app

echo "[SERVER] STARTED "
flask run