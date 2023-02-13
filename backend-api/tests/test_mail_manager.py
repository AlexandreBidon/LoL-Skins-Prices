from mail_service.mail_manager import MailManager
import unittest


class TestMailManager(unittest.TestCase):

    def test_create_mail_content(self):
        #GIVEN
        sales_data =[
            {
                "champion_name": "test",
                "skin_num": 1,
                "skin_name": "skin test",
                "current_price" : 200,
                "last_price": 400
            },
            {
                "champion_name": "test 2",
                "skin_num": 2,
                "skin_name": "skin test 2",
                "current_price" : 200,
                "last_price": 400
            },
        ]

        result = MailManager().create_mail_content(sales_data=sales_data)

        self.assertEqual(
            result,
            """<!DOCTYPE html>
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
        <img src="http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/test_1.jpg" width="300" height="300" style="margin-top:20px;">
                                <h2 style="color:#84abd9">
                                    skin test
                                </h2>
                                <h3>
                                    Current price : 200
                                    Last price : 400
                                </h3><img src="http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/test 2_2.jpg" width="300" height="300" style="margin-top:20px;">
                                <h2 style="color:#84abd9">
                                    skin test 2
                                </h2>
                                <h3>
                                    Current price : 200
                                    Last price : 400
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
        </html>"""
        )