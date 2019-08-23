import tkinter as tk
from tkinter import scrolledtext

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        def send():
            print("Found: " + recipiantInput.get())
            print("Subject: " + subjectInput.get())
            print("Email: " + str(emailInput.get("1.0",'end-1c')))
        
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

        subButton = tk.Button(self,text="Send",command=send)
        subButton.grid(column=0, row=3)

        self.pack()

    

application = App()

application.master.title("Python EMail Client (PEC)")
application.master.maxsize(720,500)

application.mainloop()
