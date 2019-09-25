import tkinter, email, smtplib, ssl, sys
from tkinter import scrolledtext, Menu, messagebox, ttk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

usersInfo = []
numberOfUsers = int(len(usersInfo)/2) # Gives integer for exact number of users. 
# ^ COULD BE USED TO DETERMINE HOW MANY BUTTONS NEEDED FOR setUser SCREEN

def popup():
    popWin = tkinter.Toplevel()
    popWin.wm_title("Input Credintials")
    popWin.maxsize(350,100)

    def pushCreds():
        global setPass
        global setUser
        setPass = passEntry.get()
        setUser = userEntry.get()
        popWin.destroy()
    
    userLabel = tkinter.Label(popWin, text="Input Username: ")
    userLabel.grid(row=0, column=0)

    userEntry = tkinter.Entry(popWin, width=40)
    userEntry.grid(row=0, column=1)

    passLabel = tkinter.Label(popWin, text="Input Password: ")
    passLabel.grid(row=1, column=0)

    passEntry = tkinter.Entry(popWin, width=40)
    passEntry.grid(row=1, column=1)

    button = tkinter.Button(popWin, text="Enter", command=pushCreds)
    button.grid(row=2, column=0)

def emailWindow():
    window = tkinter.Toplevel()
    window.wm_title("Draft EMail")
    window.maxsize(720,500)

    def buildEmail():
        recipiantEmail = recipiantInput.get()
        emailSubject = subjectInput.get()
        emailText = emailInput.get('1.0','end-1c')
        try:
            password = setPass
            senderEmail = setUser

            message = MIMEMultipart('alternative')

            message["Subject"] = str(emailSubject)
            message["From"] = str(senderEmail)
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
            server.sendmail(senderEmail, recipiantEmail, str(message))
        messagebox.showinfo("Success", "Email Sent.")
        window.destroy()

    recipiantLabel = tkinter.Label(window, text="Input Recipiant's Email: ")
    recipiantLabel.grid(column=1,row=0)

    recipiantInput = tkinter.Entry(window,width=35)
    recipiantInput.grid(column=2, row=0)

    subjectLabel = tkinter.Label(window, text="Subject:")
    subjectLabel.grid(column=1,row=1)

    subjectInput = tkinter.Entry(window,width=35)
    subjectInput.grid(column=2,row=1)

    emailInput = scrolledtext.ScrolledText(window,width=30,height=10)
    emailInput.grid(column=2,row=2)

    subButton = tkinter.Button(window,text="Send",command=buildEmail)
    subButton.grid(column=0, row=3)

def setUserWin():
    userWin = tkinter.Toplevel()
    userWin.wm_title("Set User")
    userWin.maxsize(720,500)

    usersInfo.append("pythontestingconcave@gmail.com")
    usersInfo.append("Mason_123")

    def setCreds(userName):
        global setPass
        global setUser
        if (userName == 'default'):
            setUser = usersInfo[0]
            setPass = usersInfo[1] #Instead, call for a registry entry in a file
        else:
            messagebox.showinfo("Error", "Something went wrong.")
            userWin.destroy()
        userWin.destroy()

    #Have a button creation method to accommodate infinitely sized userInfo array
    defaultUser = tkinter.Button(userWin,text="Default",command=setCreds('default'))
    defaultUser.grid(column=0,row=0)


class startWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)

        initiateEmail = tkinter.Button(self,text="Email",command=emailWindow)
        initiateEmail.grid(column=0,row=0)

        userSelect = tkinter.Button(self,text="Set User",command=setUserWin)
        userSelect.grid(column=1,row=0)

        self.pack()

root = tkinter.Tk()
m=startWindow(root)
root.title("PEC")
root.maxsize(720,500)
root.mainloop()