import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

REDIS_HOST = "127.0.0.1"
REDIS_PORT = "6379"
