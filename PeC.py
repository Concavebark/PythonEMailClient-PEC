#Imports
import tkinter, email, smtplib, ssl, sys, os.path
from tkinter import scrolledtext, Menu, messagebox, ttk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Global Variable Declation
usersInfo = []
numberOfUsers = None

#startUp function
def startUp():
    """ This function checks if the current path has 'credStorage.pec' in it
    and if it doesn't creates it.
    """
    if not(os.path.isfile('credStorage.pec')):
        createBuffer = open('credStorage.pec','w+')
        createBuffer.close()
    else:
        return(None)


def readCred():
    # reads 'credStorage.pec' and writes all read data to usersInfo and numberOfUsers 
    credBuffer = open("credStorage.pec", "r")
    global usersInfo
    global numberOfUsers
    usersInfo = credBuffer.read().split()
    numberOfUsers = int(len(usersInfo)/2)
    credBuffer.close()

def writeCred(userName, password):
    # writes new data and previous data to 'credStorage.pec'
    credBuffer = open('credStorage.pec', 'a')
    newCred = str(" " + userName + " " + password)
    credBuffer.write(newCred)
    credBuffer.close()

def deleteCred(userName):
    # deletes data from usersInfo buffer and wipes and re-writes all data to 'credStorage.pec'
    credBuffer = open('credStorage.pec', 'r+')
    bufferedInfo = credBuffer.read().split()
    try:
        indexToRemove = bufferedInfo.index(userName) 
    except ValueError:
        messagebox.showerror("Error","User Does Not Exist")
        return()
    newInfo = bufferedInfo
    passIndex = indexToRemove+1
    del newInfo[passIndex]
    del newInfo[indexToRemove]
    with open('credStorage.pec','w') as file: 
        for i in range(len(newInfo)):
            file.write(newInfo[i] + " ")
    credBuffer.close()

def deleteUser():
    #This is the function that creates the window for deleting a user
    deleteUserWin = tkinter.Toplevel()
    deleteUserWin.wm_title("Delete User")
    deleteUserWin.maxsize(700,700)

    deleteUserLabel = tkinter.Label(deleteUserWin, text="Username: ")
    deleteUserLabel.grid(row=1,column=0)

    deleteUserEntry = tkinter.Entry(deleteUserWin,width=50)
    deleteUserEntry.grid(row=1,column=1)

    def sanitizeInput():
        #sanitizes user input before sending it to deleteCred function
        thing = deleteUserEntry.get()
        deleteCred(thing)
        deleteUserWin.destroy()

    deleteUserButton = tkinter.Button(deleteUserWin,text="Delete User",command=sanitizeInput)
    deleteUserButton.grid(row=2,column=2)

def createNewUser():
    #This is the function that creates the window for creating a new user
    newUserWin = tkinter.Toplevel()
    newUserWin.wm_title("Create New User")
    newUserWin.maxsize(700,700)

    newUserLabel = tkinter.Label(newUserWin, text="New Email: ")
    newUserLabel.grid(row=1,column=0)

    newUserEntry = tkinter.Entry(newUserWin, width=50)
    newUserEntry.grid(row=1,column=1)

    newPassLabel = tkinter.Label(newUserWin, text="New Pass: ")
    newPassLabel.grid(row=2,column=0)

    newPassEntry = tkinter.Entry(newUserWin, width=50)
    newPassEntry.grid(row=2,column=1)

    def credSanitize():
        #completely sanitizes user input before sending it to writeCred function
        unsanitizedUser = newUserEntry.get()
        unsanitizedPass = newPassEntry.get()
        spaceSanitizedUser = unsanitizedUser.strip()
        spaceSanitizedPass = unsanitizedPass.strip()
        writeCred(spaceSanitizedUser, spaceSanitizedPass)
        newUserWin.destroy()

    submitNewUser = tkinter.Button(newUserWin,text="Create User",command=credSanitize)
    submitNewUser.grid(row=3,column=3)

def popup():
    #This function creates a window for inputting credentials prior to sending an email
    popWin = tkinter.Toplevel()
    popWin.wm_title("Input Credentials")
    popWin.maxsize(350,100)

    def pushCreds():
        #sends credentials to the global space to be used everywhere in the program
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
    #This is the email window
    window = tkinter.Toplevel()
    window.wm_title("Draft EMail")
    window.maxsize(720,500)

    def buildEmail():
        #this function compiles the email prior to sending it
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
        except:
            popup()

    def send(recipiantEmail, senderEmail, message, password):
        #this function sends the email
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
    #This is the function that creates the window that allows users to select their 'profile'
    userWin = tkinter.Toplevel()
    userWin.wm_title("Set User")
    userWin.maxsize(720,500)

    def credButtonCreate(self):
        #This function creates all the buttons according to how many users there are in 'credStorage.pec'
        self.buttonArray = []
        for i in range(numberOfUsers):
            nameOfUser = usersInfo[i*2].split('@',1)[0]
            self.buttonArray.append(tkinter.Button(self,text=nameOfUser,command=lambda i=i:setCreds(i)))
            self.buttonArray[i].grid(column=i+1,row=0)

    def setCreds(userName):
        #Globally sets user information depending on pressed button
        global setPass
        global setUser
        try: 
            arrayUserName = userName*2
            setUser = usersInfo[arrayUserName]
            setPass = usersInfo[arrayUserName+1]
        except:
            messagebox.showinfo("Error", 'Something went wrong.')
            userWin.destroy()
        userWin.destroy()

    readCred()
    credButtonCreate(userWin)

class startWindow(tkinter.Frame):
    #this class is the window that drives the whole program, without it, it wouldn't work.
    def __init__(self, master):
        super().__init__(master)

        startUp()

        initiateEmail = tkinter.Button(self,text="Email",command=emailWindow)
        initiateEmail.grid(column=0,row=0)

        userSelect = tkinter.Button(self,text="Set User",command=setUserWin)
        userSelect.grid(column=1,row=0)

        createUser = tkinter.Button(self,text="Create User",command=createNewUser)
        createUser.grid(column=0,row=1)

        deleteOldUser = tkinter.Button(self,text="Delete User",command=deleteUser)
        deleteOldUser.grid(column=1,row=1)

        self.pack()

root = tkinter.Tk()
m=startWindow(root)
root.title("PEC")
root.minsize(200,200)
root.mainloop()