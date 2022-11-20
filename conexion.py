import mysql.connector

con = mysql.connector.connect(
            host='192.168.100.247',
            user= 'fabrizzio',
            port= 3306,
            password = 'nousesmilinux',
            database = 'UAAMallaCurricular'
        )
cur = con.cursor()

    
def getDatosCliente():
    cur.execute(" SELECT * from Facultad")
    DatosCLie = cur.fetchall()
    print( DatosCLie)
    

getDatosCliente()