from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from Vista.UI_EstadoCarrera import Ui_EstadoCarrera
from conexion import BaseDeDatos
from eventos import *
class estadocarrera(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent = None):
        super().__init__(parent)
        self.estcarre = Ui_EstadoCarrera()
        self.estcarre.setupUi(self)
        self.parent = parent

        self.idfacultad = 0
        self.estcarre.btn_buscar.clicked.connect(lambda:self.ObtenerDato())
        self.estcarre.btn_modificar.clicked.connect(lambda:self.CambiarEstado())

    def ObtenerDato(self):
        global DatosCarrera
        codCarrera = self.estcarre.txt_codcarrera.text()
        codCarrera = int(codCarrera) 
     
        self.QueryForAll      = f"select * from carrera where idcarrera = {codCarrera}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        DatosCarrera = self.cur.fetchall()
        if(DatosCarrera != []):
            if DatosCarrera[0][3] == 1:
               EstActual =  "Activo" 
            else:
                EstActual = "Inactivo"

            self.estcarre.lbl_nombreCarrera.setText(DatosCarrera[0][2] + " - " + EstActual )
            self.estcarre.btn_modificar.setEnabled(True)
        else:
            self.estcarre.lbl_nombreCarrera.setText("No existe dicha carrera" )

    def CambiarEstado(self):
        codCarrera = self.estcarre.txt_codcarrera.text()
        if DatosCarrera[0][3]:
            NewState = 0
        else:
            NewState = 1
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(f"update carrera SET activo ={NewState} WHERE idcarrera = '{codCarrera}'")
        self.con.commit()
        self.estcarre.btn_modificar.setEnabled(False)
        self.estcarre.txt_codcarrera.clear()
        self.estcarre.lbl_nombreCarrera.clear()
        self.parent.ActualizarCarrera(self.parent.QueryForActive)
        if NewState:
            ActualState = "Activo"
        else:
            ActualState = "Inactivo"
        InfoMsg(self,'Informacion',f'Carrera se cambio a estado {ActualState} con exito')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = estadocarrera()
    mi_aplicacion.show()
    sys.exit(app.exec_())