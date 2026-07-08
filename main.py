import time
import random

from config import DELAY_MIN_SECONDS, DELAY_MAX_SECONDS, CV_PATH
from services.excel_service import ExcelService
from services.gmail_service import GmailService
from services.logger_service import LoggerService

logger = LoggerService()
gmail = GmailService()

with open("templates/correo.html", encoding="utf-8") as file:
    body = file.read()

excel = ExcelService("data/empresas.xlsx")
companies = excel.get_companies()

logger.info(f"Se encontraron {len(companies)} empresas.")

for company in companies:

    logger.info(f"Enviando correo a {company['empresa']}")

    sent = gmail.send_email(
        recipient=company["correo"],
        subject="QA Automation Engineer | Andrés Felipe Ramírez Espinal",
        body=body,
        attachment_path=CV_PATH
    )

    if sent:
        logger.success(f"Correo enviado a {company['empresa']}")
    else:
        logger.error(f"No se pudo enviar el correo a {company['empresa']}")

    delay = random.randint(DELAY_MIN_SECONDS, DELAY_MAX_SECONDS)

    logger.wait(delay)
    time.sleep(delay)

logger.success("Proceso finalizado.")