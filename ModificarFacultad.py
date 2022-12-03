from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from eventos import *


from Vista.UI_ModificarFacultad import Ui_ModificarFacultad


class modificar(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent=None):
        super().__init__(parent)
        self.modificar = Ui_ModificarFacultad()
        self.modificar.setupUi(self)
        self.parent = parent

        self.modificar.btn_buscar.clicked.connect(lambda:self.ObtenerDato())
        self.modificar.btn_modificar.clicked.connect(lambda:self.ActualizarDatos())

       
    def ObtenerDato(self):

        if self.ValidarFacultad():
            global DatosCLiente
            codFacultad = self.modificar.txt_codfacultad.text()
            codFacultad = int(codFacultad) 
            self.QueryForAll = f"select idfacultad,nombre,siglas from facultad where idfacultad = {codFacultad} and Activo = 1"
            self.connect = BaseDeDatos()
            self.con = self.connect.con
            self.cur = self.con.cursor()
            self.cur.execute(self.QueryForAll)
            DatosCLiente = self.cur.fetchall()

            if(DatosCLiente != []):
                self.modificar.txt_nombreFacultad.setText(DatosCLiente[0][1])
                self.modificar.txt_siglas.setText(DatosCLiente[0][2])
                self.HabilitarCampos(True)
            else:
                WarningMsg(self,"Atencion","Codigo de facultad no existe")


    def ValidarFacultad(self):
        codFacultad = self.modificar.txt_codfacultad.text()
        
        if not codFacultad.isnumeric():
            WarningMsg(self,"Atencion","Codigo de la facultad no es numerico")
            return False
        
        
        return True
                


    def HabilitarCampos(self,state):
        self.modificar.txt_nombreFacultad.setEnabled(state)        
        self.modificar.btn_modificar.setEnabled(state)        
        self.modificar.txt_siglas.setEnabled(state)        



    def ActualizarDatos(self):
        if self.ValidarActualizacion():
            nombreFacultad = self.modificar.txt_nombreFacultad.text()
            siglas = self.modificar.txt_siglas.text()
            
            self.connect = BaseDeDatos()
            self.con = self.connect.con
            self.cur = self.con.cursor()
            print(DatosCLiente[0][0])
            self.cur.execute(f"update facultad SET nombre = '{nombreFacultad}', siglas = '{siglas}' WHERE idfacultad = '{DatosCLiente[0][0]}'")
            self.con.commit()
            self.parent.ActualizarFacultad(self.parent.QueryForActive)
            InfoMsg(self,'Informacion','Facultad actualizada con exito')
            self.LimpiarCampos()


    def ValidarActualizacion(self):
        nombreFacultad = self.modificar.txt_nombreFacultad.text()
        siglas = self.modificar.txt_siglas.text()

        if nombreFacultad == "":
            WarningMsg(self,"Atencion","Nombre de facultad no puede estar vacio")
            return False

        if siglas == "":
            WarningMsg(self,"Atencion","Las siglas no puede estar vacio")
            return False

        return True



    def LimpiarCampos(self):
        self.modificar.txt_codfacultad.clear()
        self.modificar.txt_nombreFacultad.clear()
        self.modificar.txt_siglas.clear()
        self.HabilitarCampos(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = modificar()
    mi_aplicacion.show()
    sys.exit(app.exec_())