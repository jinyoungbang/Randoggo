import os
import smtplib
import imghdr
import config
import requests
from email.message import EmailMessage

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD
GIPHY_API_KEY = config.GIPHY_API_KEY

try:
    url = "http://api.giphy.com/v1/gifs/search"

    querystring = {"api_key":GIPHY_API_KEY,"q":"dogs","rating":"g","limit":"1"}

    headers = {
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9db8ebe-5be8-4fb4-91fd-bfc9a2bc2483,43c266a8-d847-4600-a9d4-4effcdd629bd",
        'Host': "api.giphy.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()

    # URL from GIPHY API
    doggo_url = response['data'][0]['images']["fixed_width_downsampled"]["url"]

    msg = EmailMessage()
    msg['Subject'] = "Your daily dosage of doggos!"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "jybang1999@gmail.com"
    msg.set_content("Have a great day!")

    header = "Your daily dosage of doggos!"

    html = """\
        <!DOCTYPE html>
        <html>
            <body>
                <h1>{header}</h1>
                <img src="{URL}">
            </body>
        </html>
    """.format(header=header, URL=doggo_url)

    msg.add_alternative(html, subtype="html")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("Email sent!")
except E:
    print(E)
