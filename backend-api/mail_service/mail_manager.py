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
    
    def send_sale_mail(self, sales_data, to_mail :str):
        mail_content = """<!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style type="text/css">
                h1{font-size:56px}
                h2{font-size:28px;font-weight:900}
                p{font-weight:100}
                td{vertical-align:top}
                #email{margin:auto;width:600px;background-color:#fff}
                </style>
            </head>
            <body>
                <table 
                    width="100%" 
                    height="100%" 
                    background="https://wallpapercave.com/dwp1x/wp4976096.jpg" 
                    style="background-repeat: no-repeat;
                            background-attachment: fixed;  
                            background-size: cover;"
                >
                    <tr>
                        <td width="100%" height="100%" style="backdrop-filter: blur(1.5rem) brightness(60%);">

                            <!-- "Content" table goes here -->
                            <table width="600" align="center" style="padding-top:20px;">
                                <tr>
                                    <td bgcolor="#18293D" align="center" style="color: white;">
                                        <h2>Here are the skins you like that are in sales today:</h2>
                                    </td>
                                </tr>
                                <tr>
                                    <td bgcolor="#18293D" align="center" style="color: white">
        """
        for skin in sales_data:
            skin_html = """<img src="http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/{champion_name}_{skin_num}.jpg" width="300" height="300" style="margin-top:20px;">
                                <h2 style="color:#84abd9">
                                    {skin_name}
                                </h2>
                                <h3>
                                    Current price : {current_price}
                                    Last price : {last_price}
                                </h3>""".format(
                                    champion_name = skin["champion_name"],
                                    skin_num = skin["skin_num"],
                                    skin_name = skin["skin_name"],
                                    current_price = skin["current_price"],
                                    last_price = skin["last_price"]
                                    )
            mail_content += skin_html
        mail_content +="""
        </td>
                            </tr>
                            <tr>
                                <td bgcolor="#18293D" align="center" style="color: white;">
                                    <p>
                                        We hope this mail helped you! 
                                        Have a good day!
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
            </table>
        </body>
        </html>
        """
        self.send_mail(subject="{} skins are in sale !".format(len(sales_data)), to_mail= to_mail, html_content=mail_content)