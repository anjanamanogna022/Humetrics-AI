from flask import Blueprint, render_template, request, session, redirect
import random, smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

auth = Blueprint("auth", __name__)

OTP_STORE = {}

# 👉 EMAIL CONFIG (use gmail app password)

SENDER_EMAIL = os.getenv("EMAIL_USER")
APP_PASSWORD = os.getenv("EMAIL_PASS")


def send_otp_email(to_email, otp):
    msg = EmailMessage()
    msg["Subject"] = "Your OTP Code"
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg.set_content(f"Your OTP is: {otp}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

@auth.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@auth.route("/send_otp", methods=["POST"])
def send_otp():
    name = request.form["name"]
    email = request.form["email"]

    otp = str(random.randint(100000, 999999))
    OTP_STORE[email] = otp

    session["temp_name"] = name
    session["temp_email"] = email

    send_otp_email(email, otp)

    return render_template("otp.html", email=email)

@auth.route("/verify_otp", methods=["POST"])
def verify_otp():
    entered_otp = request.form["otp"]
    email = session.get("temp_email")

    import sqlite3

    if OTP_STORE.get(email) == entered_otp:
        session["user"] = session["temp_name"]
        session["email"] = email
        session["tracking_start"] = True

    # 🔥 SAVE LOGIN
        conn = sqlite3.connect("stress.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO logins (name, email)
        VALUES (?, ?)
    """, (session["user"], email))

        conn.commit()
        conn.close()

        return redirect("/dashboard")