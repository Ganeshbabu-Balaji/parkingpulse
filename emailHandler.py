import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# create SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
print("Starting Server")

# Authentication
s.login("parkingpulseapp@gmail.com", "pslaydwoghpgbkrn")

# Create a MIMEMultipart object for the message
msg = MIMEMultipart()

# Add subject to the email
msg['Subject'] = "Important: PACE Officer Detected"

# Create the HTML body with an embedded image
html_body = """
<html>
  <body>
    <p><b style="font-size: larger;">A PACE officer has been detected near your vehicle.</b></p>
    <img src="cid:carcopguy">
  </body>
</html>
"""

msg.attach(MIMEText(html_body, 'html'))

# Embed the image directly into the email body
image_path = './carcopguy.gif'
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    image = MIMEImage(image_data, name='carcopguy.gif')
    image.add_header('Content-ID', '<carcopguy>')
    msg.attach(image)

# sending the mail
s.sendmail("parkingpulseapp@gmail.com", "parkingpulseapp@gmail.com", msg.as_string())

# terminating the session
s.quit()
print("Email Sent")
