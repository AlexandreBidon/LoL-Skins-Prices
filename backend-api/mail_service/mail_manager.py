import logging
import datetime
import smtplib
from email.message import EmailMessage
from mail_service.mail import Mail

class MailManager(Mail):

    def __init__(
        self,
        email_address = "lol.skins.prices@gmail.com",
        email_password = "wtzholqwnhshtkfm"):
        super().__init__(email_address=email_address,email_password=email_password)
    