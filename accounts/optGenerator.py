from .stuff.ygs import Password
from email.message import EmailMessage
import math, random
import ssl
import smtplib


class GenerateOpt:
    def __init__(self):
        self.corpus= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.generateOtp =""
        self.lenght = len(self.corpus)
    def generate(self, username,userEmail):
        self.generateOtp = ''
        for i in range(6):
            self.generateOtp += self.corpus[math.floor(random.random() * self.lenght)]
        email_sender = 'adudaniel097@gmail.com'
        email_password = Password().word
        email_receiver = userEmail
        subject = 'Your One-Time Password for Account Verification'
        body = f"""
        Dear {username},
        To verify your account, please enter the following One-Time Password (OTP) on the verification page:
        OTP: {self.generateOtp}
        Please note that this OTP is only valid for a single use and will expire in 5 minutes. If you did not initiate this request, please ignore this message.
        Thank you for choosing our service.
        Best regards,
        Adu Daniel's ChatBot
        """
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return self.generateOtp
    def validate(self, user,userEmail):
        email_sender = 'adudaniel097@gmail.com'
        email_password = Password().word
        email_receiver = userEmail
        subject = 'Your One-Time Password for Account Verification'
        body = f"""
Dear {user},
We are pleased to inform you that your account has been successfully verified. You can now enjoy full access to our platform and its features. Thank you for completing the verification process.
Your account details:

Username: {user}
Email: {userEmail}

If you have any questions or need assistance, please don't hesitate to contact our support team. We are here to help!
Thank you for choosing our platform.
Best regards,
Adu Daniel's ChatBot
        """
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return 'hi'
class StoreUser:
    def __init__(self):
        self.user = 'hey'
        self.Error = ''
        self.EmailValid = ''
        self.email = ''
    def store(self):
        return self.user