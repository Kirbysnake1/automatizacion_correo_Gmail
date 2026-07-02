import time

from config import DELAY_SECONDS
from services.excel_service import ExcelService
from services.gmail_service import GmailService

# Crear servicio de Gmail
gmail = GmailService()

# Leer la plantilla del correo
with open("templates/correo.txt", encoding="utf-8") as file:
    body = file.read()

# Leer empresas desde Excel
excel = ExcelService("data/empresas.xlsx")
companies = excel.get_companies()

# Enviar un correo a cada empresa
for company in companies:

    print(f"📨 Enviando correo a {company['empresa']}...")

    gmail.send_email(
        recipient=company["correo"],
        subject="QA Automation Engineer | Andrés Felipe Ramírez Espinal",
        body=body
    )

    print(f"⏳ Esperando {DELAY_SECONDS} segundos...\n")

    time.sleep(DELAY_SECONDS)