import tkinter as tk
from tkinter import scrolledtext, Menu, messagebox
import email, smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        def build():
            senderEmail = "pythontestingconcave@gmail.com"
            recipiantEmail = recipiantInput.get()
            emailSubject = subjectInput.get()
            emailText = emailInput.get('1.0','end-1c')
            
            message = MIMEMultipart('alternative')
            
            message["Subject"] = str(emailSubject)
            message["From"] = str(senderEmail) # CHANGE FOR INPUT/USER
            message["To"] = str(recipiantEmail)

            messageText = emailText
            plainText = MIMEText(messageText, 'plain') #The issue doesn't seem to be with text

            message.attach(plainText)

            send(recipiantEmail, senderEmail, message, "Mason_123")

        def send(recipiantEmail, senderEmail, message, password): #REQUIRE PASSWORD PRIOR, popup
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(senderEmail, password)
                server.sendmail(senderEmail,recipiantEmail,str(message))   
            messagebox.showinfo("Success", "Email Sent.")
            clearFields()         

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

        def clearFields():
            recipiantInput.delete('0', 'end')
            subjectInput.delete('0','end')
            emailInput.delete('1.0','end-1c')

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New Email", command=clearFields)
        fileMenu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=fileMenu) 

        self.pack()

application = App()

application.master.title("Python EMail Client (PEC)")
application.master.maxsize(720,500)

application.mainloop()