import mysql.connector

class BaseDeDatos():


    con = mysql.connector.connect(
                host='localhost',
                user= 'root',
                port= 3306,
                password = '12345',
                database = 'uaamallacurricular'
            )
    cur = con.cursor()

