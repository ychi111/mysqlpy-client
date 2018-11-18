from Classes import *
import tkinter as tk


Ins = 0
idcount = 0
windows = []


class win(object):
    """
    Класс для создания простого окна
    buttons - словарь всех созданных кнопок
    txtboxes - словарь всех созданных полей для ввода
    """
    def __init__(self, title, size):
        self.size = size
        self.root = tk.Tk()
        self.root.title = title
        self.root.geometry(self.size)
        self.root.resizable(False, False)
        self.buttons = {}
        self.txtboxes = {}

    def MainLoop(self):
        self.root.mainloop()

    def BtnCreate(self, name, func, text, side = "top"):
        btn = tk.Button(text = text, command = eval(func))
        self.buttons[name] = btn
        btn.pack(side = side)

    def TxtCreate(self, name, side = "top"):
        txtbox = tk.Entry()
        #txtbox.insert(0, "default")
        self.txtboxes[name] = txtbox
        txtbox.pack(side = side)

    def LableCreate(self, text, side = "top"):
        label = tk.Label(text = text)
        label.pack(side = side)

    def Destroy(self):
        self.root.destroy()

    def ShowButtons(self):
        #for i in self.buttons:
        print(self.buttons)
    def ShowTxtBoxes(self):
        print(self.txtboxes)

#Windows:

def RegWindow():
    global Ins
    lastx = 0
    lasty = 0
    for i in range(len(windows)):
        try:
            lastx = windows[i].root.winfo_x()
            lasty = windows[i].root.winfo_y()
            windows[i].Destroy()
        except:
            pass

    reg = win("Registration", "256x168" + "+" + str(lastx) + "+" + str(lasty))

    reg.LableCreate("Registration")
    reg.LableCreate("Login: ")
    reg.TxtCreate("loginbox")
    reg.LableCreate("Password: ")
    reg.TxtCreate("passbox")
    Ins = LazyCall(RegisterInsert, 1)

    reg.BtnCreate("makereg", "Ins", "OK")
    reg.BtnCreate("back", "AutWindow", "Back")

    windows.append(reg)
    reg.MainLoop()


def AutWindow():
    lastx = 0 
    lasty = 0
    for i in range(len(windows)):
        try:
            lastx = windows[i].root.winfo_x()
            lasty = windows[i].root.winfo_y()
            windows[i].Destroy()
        except:
            pass

    aut = win("Authorisatin", "256x180" + "+" + str(lastx) + "+" + str(lasty))

    aut.LableCreate("Authorisation")
    aut.LableCreate("Login: ")
    aut.TxtCreate("loginbox")
    aut.LableCreate("Password: ")
    aut.TxtCreate("passbox")

    aut.BtnCreate("ok", "print(\"\")", "OK")
    aut.BtnCreate("toregister", "RegWindow", "Not registered yet? Click here!")
    aut.BtnCreate("quit", "self.root.destroy", "Quit")

    windows.append(aut)
    aut.MainLoop()

#SQL FUNCTIONS:

def Select():
    db = connection()
    db.SelectCommand("SELECT * FROM users")
    db.CloseConnection()


def RegisterInsert(i):
    log = windows[i].txtboxes["loginbox"].get()
    passw = windows[i].txtboxes["passbox"].get()
    db = connection()
    db.InsertCommand("INSERT INTO users VALUES ("+str(MaxIdCounter())+", \'"+log+"\', \'"+passw+"\', 0)")
    db.CloseConnection()

def MaxIdCounter():
    db = connection()
    idcount = db.SelectCommand("SELECT MAX(id) from users")
    db.CloseConnection()
    return idcount[0]["MAX(id)"]

#Start
if __name__ == "__main__":
    AutWindow()
