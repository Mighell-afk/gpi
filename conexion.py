import mysql.connector


class BaseDeDatos:

    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user= 'root',
            port= 3306,
            password = '12345',
            database = 'uaamallacurricular'
        )
        self.cur = self.con.cursor()

    def getDatosFacultad(self):
        self.cur.execute(" select idfacultad,nombre,siglas from facultad;")
        DatosCLie = self.cur.fetchall()
     
        return DatosCLie
    
    

