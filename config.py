from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

DELAY_SECONDS = int(os.getenv("DELAY_SECONDS", "30"))