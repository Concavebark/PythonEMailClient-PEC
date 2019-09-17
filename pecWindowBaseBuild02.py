import tkinter
from tkinter import scrolledtext, Menu, messagebox, ttk
from tkinter import *
import email, smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def popup():
    window = tkinter.Toplevel()
    window.wm_title("Input Creditials")
    window.maxsize(350,100)

    def pushCreds():
        global setPass
        global setUser
        setPass = passEntry.get()
        setUser = userEntry.get()
        window.destroy()

    userLabel = tkinter.Label(window, text="Input Username: ")
    userLabel.grid(row=0, column=0)

    userEntry = tkinter.Entry(window, width=40)
    userEntry.grid(row=0, column=1)

    passLabel = tkinter.Label(window, text="Input Password: ")
    passLabel.grid(row=1, column=0)

    passEntry = tkinter.Entry(window, width=40)
    passEntry.grid(row=1, column=1)

    button = tkinter.Button(window, text="Enter", command=pushCreds)
    button.grid(row=2, column=0)



class mainWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        def build(): #instead of "Send" button going here, go straight to popup?
            recipiantEmail = recipiantInput.get()
            emailSubject = subjectInput.get()
            emailText = emailInput.get('1.0','end-1c')
            try:
                password = setPass
                senderEmail = setUser

                message = MIMEMultipart('alternative')

                message["Subject"] = str(emailSubject)
                message["From"] = str(senderEmail) # CHANGE FOR INPUT/USER
                message["To"] = str(recipiantEmail)

                messageText = emailText
                plainText = MIMEText(messageText, 'plain')

                message.attach(plainText)

                send(recipiantEmail, senderEmail, message, password)
            except NameError:
                popup()



        def send(recipiantEmail, senderEmail, message, password):
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

        #button = tkinter.Button(self,text="popup",command=popup)
        #button.grid(column=1,row=3)

        def clearFields():
            recipiantInput.delete('0', 'end')
            subjectInput.delete('0','end')
            emailInput.delete('1.0','end-1c')
            #Have this clear the active user.

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        userMenu = Menu(menubar)
        fileMenu.add_command(label="New Email", command=clearFields)
        fileMenu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=fileMenu)
        userMenu.add_command(label="pythontestingconcave@gmail.com", command=None)
        menubar.add_cascade(label="Users", menu=userMenu)

        self.pack()


root=Tk()
m=mainWindow(root)
root.title("Python EMail Client (PEC)")
root.maxsize(720,500)
root.mainloop()
