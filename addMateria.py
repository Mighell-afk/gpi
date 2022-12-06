from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import *
from Vista.ui_agregar_materia import Ui_CargarMateria
from eventos import *

class AddMate(QtWidgets.QMainWindow):
   
    

    def __init__(self,parent = None):
        super().__init__(parent)
        self.addmateria = Ui_CargarMateria()
        self.addmateria.setupUi(self)
        self.parent = parent
        self.QueryCombo = "SELECT idfacultad,nombre,siglas FROM facultad where activo = 1"
        self.CargarFacultad()
        self.addmateria.cbo_facultad.setCurrentIndex(-1)
        self.addmateria.btn_AnadirMateria.clicked.connect(lambda:self.AgregarMateria())



    #cargar el combo Box
    def CargarFacultad(self):
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryCombo)
        DatosFacultad = self.cur.fetchall()
        for i in range(len(DatosFacultad)):
            Data = DatosFacultad[i][1] +" - "+ DatosFacultad[i][2]
            id = DatosFacultad[i][0]
            self.addmateria.cbo_facultad.addItem(Data,str(id))



    def AgregarMateria(self):
        
        if self.ValidarDatos():
            try:
                codMateria = self.addmateria.txt_codfacultad.text()
                Facu_ID = int(self.addmateria.cbo_facultad.currentData())
                NombreMateria=self.addmateria.txt_siglas.text()

                self.cur.execute(f"INSERT INTO Materia(idMateria,idfacultad,Nombre) VALUES({codMateria},{Facu_ID},'{NombreMateria}') ")
                self.con.commit()
                self.parent.ActualizarMateria(self.parent.QueryForActive)
                self.LimpiarCampos()
                InfoMsg(self,'Informacion','Materia Cargada con exito')
            except mysql.connector.IntegrityError:
                CritiCalMsg(self,'Error','Codigo de la materia ya esta en uso')


    def ValidarDatos(self):
        codMateria = self.addmateria.txt_codfacultad.text()
        NombreMateria=self.addmateria.txt_siglas.text()
        
        if (not codMateria.isnumeric()) or codMateria == "":
            WarningMsg(self,'Atencion','Ingrese un numero en el codigo de materia')
            return False
        
        if self.addmateria.cbo_facultad.currentIndex() < 0:
            WarningMsg(self,'Atencion','Seleccione alguna facultad')
            return False

        if NombreMateria == "":
            WarningMsg(self,'Atencion','Ingrese un nombre de materia')
            return False
        
        return True

    def LimpiarCampos(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = AddMate()
    mi_aplicacion.show()
    sys.exit(app.exec_())
