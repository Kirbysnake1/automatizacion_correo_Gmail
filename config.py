from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
CV_PATH = os.getenv("CV_PATH")

DELAY_MIN_SECONDS = int(os.getenv("DELAY_MIN_SECONDS", "30"))
DELAY_MAX_SECONDS = int(os.getenv("DELAY_MAX_SECONDS", "59"))

if not EMAIL:
    raise ValueError("Falta EMAIL en el archivo .env")

if not APP_PASSWORD:
    raise ValueError("Falta APP_PASSWORD en el archivo .env")

if not CV_PATH:
    raise ValueError("Falta CV_PATH en el archivo .env")

if DELAY_MIN_SECONDS > DELAY_MAX_SECONDS:
    raise ValueError("DELAY_MIN_SECONDS no puede ser mayor que DELAY_MAX_SECONDS")