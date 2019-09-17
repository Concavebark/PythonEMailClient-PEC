from tkinter import *
import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.label=Label(top,text="Hello World")
        self.label.pack()
        self.entry=Entry(top)
        self.entry.pack()
        self.button=Button(top,text='Ok',command=self.cleanup)
        self.button.pack()
    def cleanup(self):
        self.value=self.entry.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.button=Button(master,text="click me!",command=self.popup)
        self.button.pack()
        self.button2=Button(master,text="print value",command=lambda: sys.stdout.write(self.entryValue()+'\n'))
        self.button2.pack()

    def popup(self):
        self.window=popupWindow(self.master)
        self.button["state"] = "disabled"
        self.master.wait_window(self.window.top)
        self.button["state"] = "normal"

    def entryValue(self):
        return self.window.value


if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
