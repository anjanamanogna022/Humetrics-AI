import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(to_email, file_path):
    msg = EmailMessage()
    msg["Subject"] = "Your Report"
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    msg.set_content("Your session report is attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="report.pdf"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)