#!/bin/bash

echo " Creating virtual environment..."
python3 -m venv .venv

echo " Activating virtual environment..."
source .venv/bin/activate

echo " Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo " Running Movie Recommendation System..."
python -m streamlit run app/web_app.py
