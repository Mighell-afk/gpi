import mysql.connector

con = mysql.connector.connect(
            host='localhost',
            user= 'root',
            port= 3306,
            password = '12345',
            database = 'uaamallacurricular'
        )
cur = con.cursor()

    
def getDatosCliente():
    cur.execute(" SELECT * from Facultad")
    DatosCLie = cur.fetchall()
    print( DatosCLie)
    

getDatosCliente()