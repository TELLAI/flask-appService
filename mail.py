import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
from dotenv import load_dotenv

if os.environ.get("my_ENV") != "production":
    load_dotenv()

def send_mail(result, email_to):
    sms = result
    mdp= os.environ.get("my_mdp")
    email= os.environ.get("my_email")
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email_to
    msg['Subject'] = 'Le sujet de mon mail' 
    s = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
    s.starttls()
    s.login(user = email, password = mdp)
    msg.attach(MIMEText(sms, 'html'))
    s.send_message(msg)