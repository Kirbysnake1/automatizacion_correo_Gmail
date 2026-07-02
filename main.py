import time

from config import DELAY_SECONDS
from services.excel_service import ExcelService
from services.gmail_service import GmailService
from services.logger_service import LoggerService

logger = LoggerService()
gmail = GmailService()

with open("templates/correo.txt", encoding="utf-8") as file:
    body = file.read()

excel = ExcelService("data/empresas.xlsx")

companies = excel.get_companies()

logger.info(f"Se encontraron {len(companies)} empresas.")

for company in companies:

    logger.info(f"Enviando correo a {company['empresa']}")

    gmail.send_email(
        recipient=company["correo"],
        subject="QA Automation Engineer | Andrés Felipe Ramírez Espinal",
        body=body
    )

    logger.success(f"Correo enviado a {company['empresa']}")

    logger.wait(DELAY_SECONDS)

    time.sleep(DELAY_SECONDS)

logger.success("Proceso finalizado.")