# INFO GATHERED FROM: https://realpython.com/python-send-email/
import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "pythontestingconcave@gmail.com"
receiver_email = "pythontestingconcave@gmail.com"
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Hi,
How are you?
Not gonna sellout lol"""
html = """\
<html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.realpython.com">Small Lie</a>
        </p>
    </body>
</html>"""

#Turning those into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

#Add both parts to MIMEMultipart message
#Email client will try to render the last part first
message.attach(part1)
message.attach(part2)

port = 465 # For ssl
password = getpass.getpass(prompt="Password: ", stream=None)

#Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    #TODO: Send email here
    server.sendmail(sender_email,receiver_email, message.as_string())

