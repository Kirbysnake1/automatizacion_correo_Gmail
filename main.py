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

subjects = [
    "QA Automation Engineer | Andrés Felipe Ramírez Espinal",
    "QA Tester / Automation Engineer | Andrés Ramírez",
    "QA Analyst | Testing Manual y Automatización | Andrés Ramírez",
    "QA Engineer | Automatización, SQL y Jira | Andrés Ramírez",
    "QA Tester | Experiencia en automatización | Andrés Ramírez",
    "QA Automation Engineer | Andrés Felipe Ramírez Espinal"
]

logger.info(f"Se encontraron {len(companies)} empresas.")

for company in companies:

    logger.info(f"Enviando correo a {company['empresa']}")
    
    subject = random.choice(subjects)


    sent = gmail.send_email(
        recipient=company["correo"],
        subject=subject,
        body=body,
        attachment_path=CV_PATH
    )

    if sent:
        logger.success(f"Correo enviado a {company['empresa']}")
        logger.subject(subject)

    else:
        logger.error(f"No se pudo enviar el correo a {company['empresa']}")

    delay = random.randint(DELAY_MIN_SECONDS, DELAY_MAX_SECONDS)

    logger.wait(delay)



logger.success("Proceso finalizado.")