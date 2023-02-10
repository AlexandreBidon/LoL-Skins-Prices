# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "lol.skins.prices@gmail.com"
email_password = "wtzholqwnhshtkfm"

# create email
msg = EmailMessage()
msg['Subject'] = "Some skins you want are currently in sale!!"
msg['From'] = email_address
msg['To'] = "alexandre.bidon.44@gmail.com"
msg.set_content("Here are the current skins in sales :")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
