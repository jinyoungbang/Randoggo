import os
import smtplib
import imghdr
import config
from email.message import EmailMessage

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD

msg = EmailMessage()
msg['Subject'] = "Your daily dosage of doggos!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = "rtchang@bu.edu"
msg.set_content("Have a great day!")

msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Your daily dosage of doggos!</h1>
            <img src="https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/200w_d.gif">
        </body>
    </html>
""", subtype="html")

with open('photo1.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = "I love dogs"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
