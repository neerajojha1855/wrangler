import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

class Settings:
    OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
    RAPIDAPI_BOOKING_KEY = os.environ.get("RAPIDAPI_BOOKING_KEY")
    OLLAMA_MODEL_NAME = os.environ.get("OLLAMA_MODEL_NAME")
    OLLAMA_HOST = os.environ.get("OLLAMA_HOST")
    DATABASE_PATH = os.environ.get("DATABASE_PATH")

settings = Settings()