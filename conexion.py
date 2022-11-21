import mysql.connector


class BaseDeDatos:

    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user= 'root',
            port= 3306,
            password = 'tuhermana',
            database = 'uaamallacurricular'
        )
        self.cur = self.con.cursor()

    
    
    

