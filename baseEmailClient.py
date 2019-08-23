import email, smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
"""
IMPORT DESCRIPTIONS
email for handling messages; also can build message packets,
smtplib for SMTP messaging,
ssl for Secure Socket Loading,
getpass for better terminal use (blind password input),
MIMEText & MIMEMultipart are used to complex message building
"""

#BULLETIN BOARD: Define separate funcs for simple & complex messages

sender_email = "pythontestingconcave@gmail.com"
receiver_email = sender_email # TESTING PURPOSES CHANGE IN FUTURE.

port = 465 #Default SSL port
password = getpass.getpass(prompt="Password: ", stream=None)

message = MIMEMultipart("alternative")
message["Subject"] = input("Subject: ")
message["From"] = sender_email
message["To"] = receiver_email # Get input here in future builds.

text = input("Message: ")

part1 = MIMEText(text, "plain")

message.attach(part1) # possibly create infinite array to allow for larger messages

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email, message.as_string())
