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
msg.set_content('''
    <!DOCTYPE html>
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
                                <img src="http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/aatrox_1.jpg" width="300" height="300" style="margin-top:20px;">
                                <h3>
                                    Aatrox
                                </h3>
                                <img src="http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/aatrox_2.jpg" width="300" height="300" style="margin-top:20px;">
                                <h3>
                                    Aatrox
                                </h3>
                                <img src="http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/aatrox_3.jpg" width="300" height="300"style="margin-top:20px;">
                                <h3>
                                    Aatrox
                                </h3>
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
''', subtype='html')
 

test = "http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/aatrox_1.jpg"
# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)