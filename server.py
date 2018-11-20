from classes import *
import socket

def MaxIdCounter():
    db = connection()
    idcount = db.SelectCommand("SELECT MAX(id) from users")
    db.CloseConnection()
    return (idcount[0]["MAX(id)"] + 1)

sock = socket.socket() #создание сокета
sock.bind(('', 9090)) #связывание сокета с любым хостом и 9090 портом
sock.listen(1) #слушаем сокет с максимальным подключением 1
conn, addr = sock.accept() #принимаем подключение, conn - новый сокет, addr - адрес клиента

#получаем данные с клиента порциями по 1024 байта:
while True:
    data = conn.recv(1024)
    if not data:
        break
    res = data.decode("utf-8").split(",")

db = connection()
db.InsertCommand("INSERT INTO users VALUES ("+str(MaxIdCounter())+", \'"+res[0]+"\', \'"+res[1]+"\', 0)")
db.CloseConnection()

conn.close() #закрываем соединение
