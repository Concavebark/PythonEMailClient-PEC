import email, smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465

def main():
    sender_email = input("Your Email: ")
    password = getpass.getpass(prompt="Password: ", stream=None)
    receiver_email = input("Recipiant's Email: ")
    buildEMail(sender_email, password, receiver_email)

def setMultiUseEmailAddr():
    user_email = input("Email: ")
    file = open("defaultEmail.txt","w")
    file.write(user_email)
    file.close()
    main()
    

def buildEMail(sender_email, password, receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = input("Subject: ")
    message["From"] = sender_email
    message["To"] = receiver_email

    text = input("Message: ")

    plainText = MIMEText(text, "plain")

    message.attach(plainText)
    send(sender_email, password, receiver_email, message)

def send(sender_email, password, receiver_email, message):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email,receiver_email,message.as_string())

main()
    
