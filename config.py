from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
CV_PATH = os.getenv("CV_PATH")
DELAY_SECONDS = int(os.getenv("DELAY_SECONDS", "30"))