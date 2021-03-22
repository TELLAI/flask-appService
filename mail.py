import smtplib, ssl 
from email.mime.text import MIMEText
from email import encoders
import os
from dotenv import load_dotenv
load_dotenv()

def send_mail(email_to):
    sms = "test"
    # sms = "***"
    mdp= os.environ.get("my_mdp")
    email= os.environ.get("my_email")
    # for i in data:
    #     for y in i:
    #         sms = sms + y + " * "
    #     sms = sms + " *** "
    msg = MIMEText(sms, 'html')
    msg['From'] = email
    msg['To'] = email_to
    msg['Subject'] = 'Le sujet de mon mail' 
    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = email, password = mdp)
    s.sendmail(email, email, msg.as_string())
    s.quit()