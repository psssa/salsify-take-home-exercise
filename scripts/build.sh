#!/bin/bash

cd ..
echo "[BUILD] Create virtual environment"
py -m venv ./venv/

pip install pandas 
pip install python-dotenv

echo "[BUILD] Activate the virtual environment"
./venv/Scripts/activate

echo "[BUILD] Install the needed modules for this project"
pip install -r requirements.txt

