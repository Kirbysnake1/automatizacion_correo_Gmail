from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")