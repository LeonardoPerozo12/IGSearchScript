import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(password: str, mail_address: str, mail_target: str):

    #credentials
    try:
        print('Email sent succesfully!')
    except Exception as e:
        print(f'Error: {e}')