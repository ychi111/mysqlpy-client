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

class LazyCall(object):
    """
        Класс создаёт ленивые функции
        То-есть при инициализации передаёте
        функцию и её параметры
        Функция не выполняется, а полученный объект
        можно будет потом вызвать как переданную
        функцию с переданными параметрами

        HOW_TO:
         def say_hi(someone):
            print("Hi, " + someone + "!")
         HiGosha = LazyCall(say_hi, "Gosha")
         HiGosha()
         "Hi, Gosha"
    """
    def __init__(self, func, *args, **kwargs):
        self.f = func
        self.a = args
        self.ka = kwargs
    def __call__(self):
        return self.f(*self.a, **self.ka)

#Можно сразу передавать параметры в функцию при её создании
#Удобно, если функция передаётся сразу в button

#Это декоратор, если чо
def lazy_callable(*args, **kwargs):
    def dec(func):
        return LazyCall(func, *args, **kwargs)
    return dec