# app/env.py
import os
from dotenv import load_dotenv
from pathlib import Path

# Go three levels up from this file (app → backend → Todo)
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
