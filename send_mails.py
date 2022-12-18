import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment vairables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject,receiver_email,name,due_date,invoice_no,amount):
    #create the base text message
    msg = EmailMessage()
    msg["subject"] = subject
    msg["From"] = formataddr(("Coding is Fun corp.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email
    
    msg.set_content(
        f"""
        Hi {name},
        I hope you are well.
        I just wanted to drop you a quick mote to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}.
        I would be really grateful if you could confirm that everything is on track for payment.
        Best regards
        DEVELOPER
        """
    )
    
#Add the html version. This converts the message into a mulpart/alternative  
    msg.add_alternative(
        f"""
        <html>
            <body>
                <p>Hi {name}</p>
                <p>I hope you are well.</p>
                <p>I just wanted to drop you a quick mote to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}.</p>
                <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
                <p>Best regards</p>
                <p>YOUR NAME</p>
            </body>
        </html>  
        """,
        subtype = "html",
    )
    
    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email,password_email)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        
if __name__ == "__main__":
    send_email(
        subject = "invoice Reminder",
        name = "Root Him",
        receiver_email="franklynekibet77@gmail.com",
        due_date = "15, Dec 2022",
        invoice_no="INV-21-12-009",
        amount = "5",
        )