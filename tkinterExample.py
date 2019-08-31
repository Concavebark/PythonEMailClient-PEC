import tkinter as tk
from tkinter import Menu

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.initUI()

    #MENUBAR info gathered from http://zetcode.com/tkinter/menustoolbars/

    def initUI(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.quit = tk.Button(self, text="QUIT", fg="red", command = self.master.destroy)

        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
