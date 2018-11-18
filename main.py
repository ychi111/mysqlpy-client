from Classes import *
import tkinter as tk


Temp = 0


class Win(object):
    """
    Класс для создания простого окна
    buttons - словарь всех созданных кнопок
    txtboxes - словарь всех созданных полей для ввода
    """
    def __init__(self):
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

class AutWindow(Win):

    def build(self, x = 100, y = 100):
        self.root = tk.Tk()
        self.root.size = "256x180" + "+" + str(x) + "+" + str(y)
        self.root.title = "Authorisation"
        self.root.geometry(self.root.size)
        self.root.resizable(False, False)
        self.LableCreate("Authorisation")
        self.LableCreate("Login: ")
        self.TxtCreate("loginbox")
        self.LableCreate("Password: ")
        self.TxtCreate("passbox")
        self.BtnCreate("ok", "self.AutCheck", "OK")
        self.BtnCreate("toregister", "self.switch_window", "Not registered yet? Click here!")
        self.BtnCreate("quit", "self.Destroy", "Quit")
        self.MainLoop()

    def switch_window(self):
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        self.Destroy()
        windows["RegWindow"].build(x, y)

    def AutCheck(self):
        log = windows["AutWindow"].txtboxes["loginbox"].get()
        passw = windows["AutWindow"].txtboxes["passbox"].get()
        db = connection()
        if (log!="" and passw!=""):
            privileges = db.SelectCommand("SELECT privileges FROM users WHERE (login = \""+log+"\" and password = \""+passw+"\")")
        else:
            print('login or password box is empty!')
        db.CloseConnection()
        print(privileges[0]["privileges"])

class RegWindow(Win):

    def build(self, x = 100, y = 100):
        self.root = tk.Tk()
        self.root.size = "256x168" + "+" + str(x) + "+" + str(y)
        self.root.title = "Registration"
        self.root.geometry(self.root.size)
        self.root.resizable(False, False)
        self.LableCreate("Registration")
        self.LableCreate("Login: ")
        self.TxtCreate("loginbox")
        self.LableCreate("Password: ")
        self.TxtCreate("passbox")
        self.BtnCreate("makereg", "self.RegInsert", "OK")
        self.BtnCreate("back", "self.switch_window", "Back")
        self.MainLoop()

    def switch_window(self):
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        self.Destroy()
        windows["AutWindow"].build(x, y)

    def RegInsert(self):
        log = windows["RegWindow"].txtboxes["loginbox"].get()
        passw = windows["RegWindow"].txtboxes["passbox"].get()
        db = connection()
        if (log!="" and passw!=""):
            db.InsertCommand("INSERT INTO users VALUES ("+str(MaxIdCounter())+", \'"+log+"\', \'"+passw+"\', 0)")
        else:
            print('login or password box is empty!')
        db.CloseConnection()

#SQL FUNCTIONS:

def Select():
    db = connection()
    db.SelectCommand("SELECT * FROM users")
    db.CloseConnection()


def MaxIdCounter():
    db = connection()
    idcount = db.SelectCommand("SELECT MAX(id) from users")
    db.CloseConnection()
    return (idcount[0]["MAX(id)"] + 1)
###############################################

#Start
if __name__ == "__main__":

    windows = {}

    AutWindow = AutWindow()
    RegWindow = RegWindow()

    windows["AutWindow"] = AutWindow
    windows["RegWindow"] = RegWindow

    AutWindow.build()
