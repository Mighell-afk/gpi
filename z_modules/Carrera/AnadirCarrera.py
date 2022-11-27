from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from z_modules.conexion import BaseDeDatos
from z_modules.eventos import *
from Vista.Carrera.UI_AgregarCarrera import Ui_AgregarCarrera


class AddCarrera(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent=None):
        
        super().__init__(parent)
        self.UI_AgregarCarrera = Ui_AgregarCarrera()
        self.UI_AgregarCarrera.setupUi(self)
        self.parent=parent
        self.connect=BaseDeDatos()
        self.con=self.connect.con
        self.cur=self.con.cursor()


        self.UI_AgregarCarrera.btn_AnadirCarrera.clicked.connect(lambda:self.AnadirDatos())

        


        
    def AnadirDatos(self):
        if self.ValidarDatos():
            codFacu = self.Addfacu.txt_codfacultad.text()
            nombrefacu=self.Addfacu.txt_nombreFacultad.text()
            siglas=self.Addfacu.txt_siglas.text()

            self.cur.execute(f"INSERT INTO facultad(idfacultad,nombre,siglas) VALUES({codFacu},'{nombrefacu}','{siglas}') ")
            self.con.commit()
            self.parent.ActualizarFacultad(self.parent.QueryForActive)
            self.LimpiarCampos()
            InfoMsg(self,'Informacion','Facultad Cargada con exito')

            



    def ValidarDatos(self):
        codFacu = self.Addfacu.txt_codfacultad.text()
        nombrefacu = self.Addfacu.txt_nombreFacultad.text()
        siglas = self.Addfacu.txt_siglas.text()
        
        if not codFacu.isnumeric():
            WarningMsg(self,"Atencion","Codigo de la facultad no es numerico")
            return False

        if nombrefacu == "":
            WarningMsg(self,"Atencion","Ingrese el nombre de la facultad")
            return False
  
        if siglas == "":
            WarningMsg(self,"Atencion","Ingrese las siglas de la facultad")
            return False

        return True


    def LimpiarCampos(self):
        self.Addfacu.txt_codfacultad.clear()
        self.Addfacu.txt_nombreFacultad.clear()
        self.Addfacu.txt_siglas.clear()
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = Ui_AgregarCarrera()
    mi_aplicacion.show()
    sys.exit(app.exec_())