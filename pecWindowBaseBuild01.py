import tkinter as tk
from tkinter import scrolledtext
import email, smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        def build():
            senderEmail = "pythontestingconcave@gmail.com"
            recipiantEmail = recipiantInput.get()
            emailSubject = subjectInput.get()
            emailText = str(emailInput.get('1.0','end-1c'))
            
            message = MIMEMultipart('alternative')
            print(emailSubject)
            print(str(emailSubject))
            message["Subject"] = str(emailSubject)
            message["From"] = senderEmail # CHANGE FOR INPUT/USER
            message["To"] = recipiantEmail

            messageText = emailText
            plainText = MIMEText(messageText, 'plain')

            message.attach(plainText)

            send(recipiantEmail, senderEmail, emailSubject, message, "Mason_123")

        def send(recipiantEmail, senderEmail, emailSubject, message, password): #REQUIRE PASSWORD PRIOR, popup
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
                server.login(senderEmail, password) # Next line crashes. Possible problem with the message
                server.sendmail(senderEmail,recipiantEmail,message) #CLEAR EVERYTHING AFTER SENDING EMAIL


        
        recipiantLabel = tk.Label(self, text="Input Recipiant's Email: ")
        recipiantLabel.grid(column=1,row=0)

        recipiantInput = tk.Entry(self,width=35)
        recipiantInput.grid(column=2, row=0)

        subjectLabel = tk.Label(self, text="Subject:")
        subjectLabel.grid(column=1,row=1)

        subjectInput = tk.Entry(self,width=35)
        subjectInput.grid(column=2,row=1)

        emailInput = scrolledtext.ScrolledText(self,width=30,height=10)
        emailInput.grid(column=2,row=2)        

        subButton = tk.Button(self,text="Send",command=build)
        subButton.grid(column=0, row=3)

        self.pack()

    

application = App()

application.master.title("Python EMail Client (PEC)")
application.master.maxsize(720,500)

application.mainloop()
