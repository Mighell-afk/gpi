from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import *
from eventos import *
from Vista.UI_Addfacu import Ui_AnadirFacultad


class Addfacu(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent=None):
        
        super().__init__(parent)
        self.Addfacu = Ui_AnadirFacultad()
        self.Addfacu.setupUi(self)
        self.parent=parent
        self.connect=BaseDeDatos()
        self.con=self.connect.con
        self.cur=self.con.cursor()


        self.Addfacu.btn_AnadirFacultad.clicked.connect(lambda:self.AnadirDatos())

        


        
    def AnadirDatos(self):
        if self.ValidarDatos():
            codFacu = self.Addfacu.txt_codfacultad.text()
            nombrefacu=self.Addfacu.txt_nombreFacultad.text()
            siglas=self.Addfacu.txt_siglas.text()
            try:
                self.cur.execute(f"INSERT INTO facultad(idfacultad,nombre,siglas) VALUES({codFacu},'{nombrefacu}','{siglas}') ")
                self.con.commit()
                self.parent.ActualizarFacultad(self.parent.QueryForActive)
                self.LimpiarCampos()
                InfoMsg(self,'Informacion','Facultad Cargada con exito')
            except mysql.connector.IntegrityError:
                CritiCalMsg(self,'Error',f'Codigo de la facultad ya esta en uso')
            
            



    def ValidarDatos(self):
        codFaq = self.Addfacu.txt_codfacultad.text()
        nombrefacu = self.Addfacu.txt_nombreFacultad.text()
        siglas = self.Addfacu.txt_siglas.text()
        
        if not codFaq.isnumeric():
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
    mi_aplicacion = Addfacu()
    mi_aplicacion.show()
    sys.exit(app.exec_())