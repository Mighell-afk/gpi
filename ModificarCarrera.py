from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from eventos import *


from Vista.UI_ModiCarrera import Ui_ModiCarrera


class modificar(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent=None):
        super().__init__(parent)
        self.modificarcarrera = Ui_ModiCarrera()
        self.modificarcarrera.setupUi(self)
        self.parent = parent

        self.QueryCombo = "SELECT idfacultad,nombre,siglas FROM facultad where activo = 1"
        self.modificarcarrera.btn_buscar.clicked.connect(lambda:self.ObtenerDatos())
        self.modificarcarrera.btn_modificar.clicked.connect(lambda:self.ActualizarDatos())

    def ObtenerDatos(self):
        global DatosMateria
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        id = self.modificarcarrera.txt_codcarrera.text()
        self.cur.execute(f" SELECT ca.idcarrera,ca.nombre,fa.nombre as facultad FROM carrera ca inner join facultad fa on (ca.idfacultad = fa.idfacultad) WHERE ca.idcarrera = {int(id)} and ca.activo =1;")
        DatosMateria = self.cur.fetchall()

        if DatosMateria != []:
            self.modificarcarrera.txt_nombreCarrera.setText(str(DatosMateria[0][1]))
            self.idfacultad = 0

            self.CargarComboBox()
            self.HabilitarCampos(True)
        else:
            self.modificarcarrera.txt_nombreCarrera.setText("Carrera con ese codigo no existe")

    def CargarComboBox(self):
        
        global id
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryCombo)
        allfacus = []
        DatosFacultad = self.cur.fetchall()
        self.modificarcarrera.cbo_Facultad.clear()
        for i in range(len(DatosFacultad)):
            Data = DatosFacultad[i][1] +" - "+ DatosFacultad[i][2]
            id = DatosFacultad[i][0]
            self.modificarcarrera.cbo_Facultad.addItem(Data,str(id))
            allfacus.append(DatosFacultad[i][1])
        #poner el que cargo el usuario
        self.modificarcarrera.cbo_Facultad.findText(str(DatosMateria[0][2]),Qt.MatchFixedString)
        index = 0
        for i in range(len(allfacus)):
            if allfacus[i] == DatosMateria[0][2]:
                break
            else:
                index += 1 
        self.modificarcarrera.cbo_Facultad.setCurrentIndex(index)
       
    

    def HabilitarCampos(self,state):

        self.modificarcarrera.txt_nombreCarrera.setEnabled(state)        
        self.modificarcarrera.btn_modificar.setEnabled(state)        
        self.modificarcarrera.cbo_Facultad.setEnabled(state)        

    def ActualizarDatos(self):

        FacuID = self.modificarcarrera.cbo_Facultad.currentData()
        NombreCarre = self.modificarcarrera.txt_nombreCarrera.text()

        self.cur.execute(f" UPDATE carrera SET idfacultad = {FacuID}, Nombre = '{NombreCarre}' WHERE idcarrera = {int(DatosMateria[0][0])}  ")
        #print(DatosMateria[0][0])
        self.con.commit()
        self.parent.ActualizarCarrera(self.parent.QueryForActive)
        self.LimpiarCampos()

    def LimpiarCampos(self):
        self.HabilitarCampos(False)
        self.modificarcarrera.txt_nombreCarrera.clear()
        self.modificarcarrera.cbo_Facultad.setCurrentIndex(-1)
        self.modificarcarrera.txt_codcarrera.clear()

        self.HabilitarCampos(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = modificar()
    mi_aplicacion.show()
    sys.exit(app.exec_())