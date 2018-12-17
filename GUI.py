from requests import *
import tkinter as tk


class Win(object):
    """
    Класс для создания простого окна (от него наследуются все остальные классы - окна)
    buttons - словарь всех созданных кнопок
    txtboxes - словарь всех созданных полей для ввода
    labels - словарь добавленных текстов
    """

    def __init__(self):
        self.buttons = {}
        self.txtboxes = {}
        self.labels = {}

    def MainLoop(self):
        self.root.mainloop()

    def BtnCreate(self, name, func, text, side = "top"):
        btn = tk.Button(text = text, command = eval(func))
        self.buttons[name] = btn
        btn.pack(side = side)

    def TxtCreate(self, name, side = "top", show = ""):
        txtbox = tk.Entry(show = show)
        #txtbox.insert(0, "default")
        self.txtboxes[name] = txtbox
        txtbox.pack(side = side)

    def LableCreate(self, text, side = "top", name = ""):
        label = tk.Label(text = text)
        label.pack(side = side)
        if (name):
            self.labels[name] = label

    def Destroy(self):
        self.root.destroy()

class UserWindow(Win):
    """
    Класс для создания окна пользователя
    """

    def build(self, x = 100, y = 100):
        self.root = tk.Tk()
        self.root.size = "256x256" + "+" + str(x) + "+" + str(y)
        self.root.title = "User"
        self.root.geometry(self.root.size)
        self.root.resizable(False, False)
        self.LableCreate("User Window")
        self.BtnCreate("quit", "self.Destroy", "Quit")
        self.MainLoop()

class AdminWindow(Win):
    """
    Класс для создания окна администрирования
    """

    def build(self, x = 100, y = 100):
        self.root = tk.Tk()
        self.root.size = "256x256" + "+" + str(x) + "+" + str(y)
        self.root.title = "Administration"
        self.root.geometry(self.root.size)
        self.root.resizable(False, False)
        self.LableCreate("Admin Window")
        self.BtnCreate("quit", "self.Destroy", "Quit")
        self.MainLoop()

class AutWindow(Win):
    """
    Класс для создания окна авторизации
    """

    def build(self, x = 100, y = 100):
        self.root = tk.Tk()
        self.root.size = "256x185" + "+" + str(x) + "+" + str(y)
        self.root.title = "Authorisation"
        self.root.geometry(self.root.size)
        self.root.resizable(False, False)
        self.LableCreate("Authorisation")
        self.LableCreate("Login: ")
        self.TxtCreate("loginbox")
        self.LableCreate("Password: ")
        self.TxtCreate("passbox", "top", "*")
        self.BtnCreate("ok", "self.aut_ok", "OK")
        self.BtnCreate("toregister", "self.switch_window", "Not registered yet? Click here!")
        self.BtnCreate("quit", "self.Destroy", "Quit")
        self.MainLoop()

    def switch_window(self):
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        self.Destroy()
        windows["RegWindow"].build(x, y)

    def aut_ok(self):
        if (self.aut_check() == 0):
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            self.Destroy()
            windows["UserWindow"].build(x, y)
        elif (self.aut_check() == 1):
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            self.Destroy()
            windows["AdminWindow"].build(x, y)
    def aut_check(self):
        log = windows["AutWindow"].txtboxes["loginbox"].get()
        passw = windows["AutWindow"].txtboxes["passbox"].get()
        db = connection()
        if (log!="" and passw!=""):
            privileges = db.SelectCommand("SELECT privileges FROM users WHERE (login = \""+log+"\" and password = \""+passw+"\")")
        else:
            print('login or password box is empty!')
        db.CloseConnection()
        return(privileges[0]["privileges"])

class RegWindow(Win):
    """
    Класс для создания окна регистрации
    """

    def build(self, x = 100, y = 100):
        self.root = tk.Tk()
        self.root.size = "256x220" + "+" + str(x) + "+" + str(y)
        self.root.title = "Registration"
        self.root.geometry(self.root.size)
        self.root.resizable(False, False)
        self.LableCreate("Registration")
        self.LableCreate("Login: ")
        self.TxtCreate("loginbox")
        self.LableCreate("Password: ")
        self.TxtCreate("passbox1", "top", "*")
        self.LableCreate("Repeat password please: ")
        self.TxtCreate("passbox2", "top", "*")
        self.BtnCreate("makereg", "self.reg_insert", "OK")
        self.BtnCreate("back", "self.switch_window", "Back")
        self.LableCreate("", "top", "error")
        self.MainLoop()

    def switch_window(self):
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        self.Destroy()
        windows["AutWindow"].build(x, y)

    def reg_insert(self):
        log = windows["RegWindow"].txtboxes["loginbox"].get()
        passw1 = windows["RegWindow"].txtboxes["passbox1"].get()
        passw2 = windows["RegWindow"].txtboxes["passbox2"].get()
        if (passw1 == passw2):
            if (log!="" and passw1!=""):
                reg_insert(log, passw1)
            else:
                print('login or password box is empty!')
        else:
            windows["RegWindow"].labels["error"].config(text = "Passwords are not equal!")

windows = {}
