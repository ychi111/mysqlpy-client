import pymysql


class connection(object):
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='1234',
                                         db='Octave',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        except:
            print("Connection failed!")
    def SelectCommand(self, text):
        self.text = text
        try:
            with self.connection.cursor() as self.cursor:
                # SQL
                self.sql = self.text
                print(self.sql)
                # Выполнить команду запроса (Execute Query).
                self.cursor.execute(self.sql)
                retrow = []
                for row in self.cursor:
                    retrow.append(row)
                return (retrow)
        except:
            print("Command Error!")
            
    def CloseConnection(self):
        self.connection.close()

    def InsertCommand(self, text):
        self.text = text
        try:
            with self.connection.cursor() as self.cursor:
                # SQL
                self.sql = self.text
                print(self.sql)
                # Выполнить команду запроса (Execute Query).
                self.cursor.execute(self.sql)
                self.connection.commit()
        except:
            print("Command Error!")
    def CloseConnection(self):
        self.connection.close()
