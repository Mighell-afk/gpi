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

        codCarrera = self.UI_AgregarCarrera.txt_codCarrera.text()
        nombreCarrera= self.UI_AgregarCarrera.txt_nombreCarrera.text()
        sql = "SELECT idfacultad, nombre FROM facultad"
        self.cur.execute(sql)
        DatosFacultad = self.cur.fetchall()
        listafacultad = []
        for facultad in DatosFacultad:
            listafacultad.append(f"{facultad[0]} - {facultad[1]}")

        self.UI_AgregarCarrera.cboFacultad.addItems(listafacultad)
        self.UI_AgregarCarrera.cboFacultad.setCurrentIndex(-1)
        print(DatosFacultad)
    
        
    def AnadirDatos(self):
        if self.ValidarDatos():  
            codCarrera = self.UI_AgregarCarrera.txt_codCarrera.text()
            nombreCarrera= self.UI_AgregarCarrera.txt_nombreCarrera.text()
            facu = self.UI_AgregarCarrera.cboFacultad.currentIndex()
            self.cur.execute(f"INSERT INTO carrera(idfacultad,idcarrera,nombre) VALUES ( {facu},'{codCarrera}','{nombreCarrera}') ")
            self.con.commit()
            self.parent.ActualizarFacultad(self.parent.QueryForActive)
            self.LimpiarCampos()
            InfoMsg(self,'Informacion','Facultad Cargada con exito')
          
            



    def ValidarDatos(self):
        codCarrera = self.UI_AgregarCarrera.txt_codCarrera.text()
        nombreCarrera = self.UI_AgregarCarrera.txt_nombreCarrera.text()
        
        
        if not codCarrera.isnumeric():
            WarningMsg(self,"Atencion","Codigo de la carrera no es numerico")
            return False

        if nombreCarrera == "":
            WarningMsg(self,"Atencion","Ingrese el nombre de la facultad")
            return False

        return True


    def LimpiarCampos(self):
        self.self.UI_AgregarCarrera.txt_codCarrera.clear()
        self.UI_AgregarCarrera.txt_nombreCarrera.clear()
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = Ui_AgregarCarrera()
    mi_aplicacion.show()
    sys.exit(app.exec_())