from bd_connect import *


#SQL FUNCTIONS:

def select():
    db = connection()
    db.SelectCommand("SELECT * FROM users")
    db.CloseConnection()

def reg_insert(log, passw):
    db = connection()
    db.InsertCommand("INSERT INTO users VALUES ("+str(max_id_counter())+", \'"+log+"\', \'"+passw+"\', 0)")
    db.CloseConnection()

def max_id_counter():
    db = connection()
    idcount = db.SelectCommand("SELECT MAX(user_id) from users")
    db.CloseConnection()
    return (idcount[0]["MAX(user_id)"] + 1)
