from client import *


AutWindow = AutWindow()
RegWindow = RegWindow()
AdminWindow = AdminWindow()
UserWindow = UserWindow()

windows["AutWindow"] = AutWindow
windows["RegWindow"] = RegWindow
windows["AdminWindow"] = AdminWindow
windows["UserWindow"] = UserWindow

AutWindow.build()
