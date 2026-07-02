import logging
import os


class LoggerService:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        self.logger = logging.getLogger("gmail_automation")

        # Evita duplicar logs si el servicio se crea más de una vez
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

    def wait(self, seconds):
        print(f"⏳ Esperando {seconds} segundos...")
        self.logger.info(f"Esperando {seconds} segundos")