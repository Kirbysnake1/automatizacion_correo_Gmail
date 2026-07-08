import os
import smtplib
from email.message import EmailMessage

from config import EMAIL, APP_PASSWORD


class GmailService:

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    def __init__(self):
        self.email = EMAIL
        self.password = APP_PASSWORD.replace(" ", "")

    def send_email(self, recipient, subject, body, attachment_path=None):

        try:

            message = EmailMessage()

            message["From"] = self.email
            message["To"] = recipient
            message["Subject"] = subject

            # Texto plano (fallback)
            message.set_content(
                "Este correo contiene una versión HTML. Si no puedes verla, utiliza un cliente compatible."
            )

            # HTML
            message.add_alternative(body, subtype="html")

            # Adjuntar archivo
            if attachment_path:

                with open(attachment_path, "rb") as file:

                    message.add_attachment(
                        file.read(),
                        maintype="application",
                        subtype="pdf",
                        filename=os.path.basename(attachment_path)
                    )

            with smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT) as smtp:

                smtp.login(self.email, self.password)
                smtp.send_message(message)

            return True

        except Exception as e:

            print(e)
            return False