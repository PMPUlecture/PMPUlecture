from django.shortcuts import redirect

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os


def auth_allowed(backend, details, response, **kwargs):
    if not backend.auth_allowed(response, details):
        msg = MIMEMultipart()
        message = f"""Кто-то пытался зайти не под студенческой почтой! Вот его данные:
        
        username: {details['username']}
        email: {details['email']}
        fullname: {details['fullname']}
        first_name: {details['first_name']}
        last_name: {details['last_name']}
        """

        password = os.environ.get('email_password')
        msg['From'] = "pmpulecture@bk.ru"
        msg['To'] = "pmpulecture@bk.ru"
        msg['Subject'] = "Кто-то пытался зайти не под студенческой почтой!"

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.bk.ru: 587')
        server.starttls()
        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        return redirect('/login/?error=2')
