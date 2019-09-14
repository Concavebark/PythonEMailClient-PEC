import tkinter
from tkinter import scrolledtext, Menu, messagebox
from tkinter import *
import email, smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class popupWindow(object):
    def __init__(self, master):
        top=self.top=Toplevel(master)

        button = tkinter.Button(self,text="Enter",command=self.cleanup)
        button.grid(column=1,row=1)

        inputField = tkinter.Entry(self,width=50)
        inputField.grid(column=1,row=0)

        button.pack()
        inputField.pack()

    def cleanup(self):
        self.value = self.master.inputField.get()
        self.destroy()

class mainWindow(object):
    def __init__(self, master):
        #super().__init__(master)

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

        recipiantLabel = tkinter.Label(self, text="Input Recipiant's Email: ")
        recipiantLabel.grid(column=1,row=0)

        recipiantInput = tkinter.Entry(self,width=35)
        recipiantInput.grid(column=2, row=0)

        subjectLabel = tkinter.Label(self, text="Subject:")
        subjectLabel.grid(column=1,row=1)

        subjectInput = tkinter.Entry(self,width=35)
        subjectInput.grid(column=2,row=1)

        emailInput = scrolledtext.ScrolledText(self,width=30,height=10)
        emailInput.grid(column=2,row=2)        

        subButton = tkinter.Button(self,text="Send",command=build)
        subButton.grid(column=0, row=3)
        button = tkinter.Button(self,text="popup",command=self.popUp)
        button.grid(column=1,row=3)

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

    def popUp(self):
            self.w=popupWindow(self.master)
            self.master.wait_window(self.w.top)

if __name__ == '__main__':
    root=Tk()
    m=mainWindow(root)
    root.title("Python EMail Client (PEC)")
    root.maxsize(720,500)
    root.mainloop()