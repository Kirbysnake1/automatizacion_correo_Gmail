import logging
import os
import sys
import time


class LoggerService:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        self.logger = logging.getLogger("gmail_automation")

        if self.logger.handlers:
            return

        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d/%m/%Y %H:%M:%S"
        )

        file_handler = logging.FileHandler(
            "logs/app.log",
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message):
        print(f"ℹ️  {message}")
        self.logger.info(message)

    def success(self, message):
        print(f"✅ {message}")
        self.logger.info(message)

    def warning(self, message):
        print(f"⚠️ {message}")
        self.logger.warning(message)

    def error(self, message):
        print(f"❌ {message}")
        self.logger.error(message)

    def subject(self, subject):
        print(f"📨 Subject enviado: {subject}")
        self.logger.info(f"Subject enviado: {subject}")

    def wait(self, seconds):
        print(f"⏳ Tiempo configurado de espera: {seconds} segundos")
        self.logger.info(f"Tiempo configurado de espera: {seconds} segundos")

        for remaining in range(seconds, 0, -1):
            sys.stdout.write(
                f"\r⌛ Faltan {remaining:02d} segundos para el siguiente correo..."
            )
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write("\r✅ Espera finalizada.                                \n")
        sys.stdout.flush()