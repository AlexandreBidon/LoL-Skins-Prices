import logging
import datetime
import smtplib
from email.message import EmailMessage

class Mail():

    def __init__(
        self,
        email_address = "lol.skins.prices@gmail.com",
        email_password = "wtzholqwnhshtkfm"):
        self.email_address = email_address
        self.email_password = email_password
    
    def send_mail(
        self,
        subject : str,
        to_mail : str,
        html_content : str
    ):
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.email_address
            msg['To'] = to_mail
            msg.set_content(html_content, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_address, self.email_password)
                smtp.send_message(msg)
            logging.info("Sending mail to {}".format(to_mail))
        except Exception as e:
            logging.info("Couldn't send mail to {}".format(to_mail))
            logging.error(e)

