from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
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
        #self.addmateria.cbo_facultad.currentIndexChanged.connect(self.printconsole)
 
    # def printconsole(self,index):
    #     print("Producto:",self.addmateria.cbo_facultad.itemText(index),"id: ",self.addmateria.cbo_facultad.itemData(index))
        
    def AgregarMateria(self):
        codMateria = self.addmateria.txt_codfacultad.text()
        Facu_ID = int(self.addmateria.cbo_facultad.currentData())
        # print(id)
        NombreMateria=self.addmateria.txt_siglas.text()

        self.cur.execute(f"INSERT INTO Materia(idMateria,Facultad_ID,Nombre) VALUES({codMateria},{Facu_ID},'{NombreMateria}') ")
        self.con.commit()
        self.parent.ActualizarMateria(self.parent.QueryForActive)
        #self.LimpiarCampos()
        InfoMsg(self,'Informacion','Facultad Cargada con exito')






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = AddMate()
    mi_aplicacion.show()
    sys.exit(app.exec_())
