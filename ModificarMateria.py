from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from Vista.ui_modificarMateria import Ui_MdificarMateria
from eventos import *

class ModificarMateria(QtWidgets.QMainWindow):
   
    

    def __init__(self,parent = None):
        super().__init__(parent)
        self.modmateria = Ui_MdificarMateria()
        self.modmateria.setupUi(self)
        self.parent = parent
        self.QueryCombo = "SELECT idfacultad,nombre,siglas FROM facultad where activo = 1"
        self.modmateria.btn_buscar.clicked.connect(lambda:self.ObtenerDatos())

    
    def ObtenerDatos(self):
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        id = self.modmateria.txt_codMateria.text()
        self.cur.execute(f"SELECT idMateria,Facultad_ID,Nombre FROM materia where idMateria = {int(id)} and Activo = 1;")
        DatosMateria = self.cur.fetchall()
        print(DatosMateria)
        if DatosMateria != []:
            self.modmateria.txt_nombreMateria.setText(str(DatosMateria[0][2]))
            self.CargarFacultad()
            self.HabilitarCampos(True)
        else:
            self.modmateria.txt_nombreMateria.setText("Materia con ese codigo no existe")

    def CargarFacultad(self):
        global id
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryCombo)
        DatosFacultad = self.cur.fetchall()
        for i in range(len(DatosFacultad)):
            Data = DatosFacultad[i][1] +" - "+ DatosFacultad[i][2]
            id = DatosFacultad[i][0]
            self.modmateria.cbo_Facultad.addItem(Data,str(id))

            
    def HabilitarCampos(self,state):
        self.modmateria.txt_nombreMateria.setEnabled(state)
        self.modmateria.cbo_Facultad.setEnabled(state)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = ModificarMateria()
    mi_aplicacion.show()
    sys.exit(app.exec_())
