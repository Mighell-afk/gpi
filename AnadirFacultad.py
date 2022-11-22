from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
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
        codFacu = self.Addfacu.txt_codfacultad.text()
        nombrefacu=self.Addfacu.txt_nombreFacultad.text()
        siglas=self.Addfacu.txt_siglas.text()

        self.cur.execute(f"INSERT INTO facultad(idfacultad,nombre,siglas) VALUES({codFacu},'{nombrefacu}','{siglas}') ")
        self.con.commit()
        self.parent.ActualizarFacultad(self.parent.QueryForActive)
        self.LimpiarCampos()
        InfoMsg(self,'Informacion','Facultad Cargada con exito')


    def LimpiarCampos(self):
        self.Addfacu.txt_codfacultad.clear()
        self.Addfacu.txt_nombreFacultad.clear()
        self.Addfacu.txt_siglas.clear()
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = Addfacu()
    mi_aplicacion.show()
    sys.exit(app.exec_())