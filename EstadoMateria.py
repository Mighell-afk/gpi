from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from Vista.ui_estadoMateria import Ui_EstadoMateria
from conexion import BaseDeDatos
from eventos import *

class estmate(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent = None):
        super().__init__(parent)
        self.estfacu = Ui_EstadoMateria()
        self.estfacu.setupUi(self)
        self.parent = parent
        self.estfacu.btn_buscar.clicked.connect(lambda:self.ObtenerDato())
        self.estfacu.btn_cambiarEstado.clicked.connect(lambda:self.CambiarEstado())

    def ObtenerDato(self):
        global DatosMate
        codMate = int(self.estfacu.txt_codmateria.text())
     
        self.QueryForAll      = f"select * from materia where idMateria = {codMate}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        DatosMate = self.cur.fetchall()
        if(DatosMate != []):
            if DatosMate[0][3] == 1:
               EstActual =  "Activo" 
            else:
                EstActual = "Inactivo"

            # print(DatosMate[0][1], " - ",EstActual)
            self.estfacu.lbl_nombremateria.setText(DatosMate[0][2] + " - " + EstActual)
            self.estfacu.btn_cambiarEstado.setEnabled(True)
        else:
            self.estfacu.lbl_nombremateria.setText("No existe dicha materia" )



    def CambiarEstado(self):
        codFacultad = self.estfacu.txt_codmateria.text()
        if DatosMate[0][3]:
            NewState = 0
        else:
            NewState = 1
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(f"update materia SET activo ={NewState} WHERE idMateria = '{codFacultad}'")
        self.con.commit()
        self.estfacu.btn_cambiarEstado.setEnabled(False)
        self.estfacu.txt_codmateria.clear()
        self.estfacu.lbl_nombremateria.clear()
        self.parent.ActualizarMateria(self.parent.QueryForActive)
        if NewState:
            ActualState = "Activo"
        else:
            ActualState = "Inactivo"
        InfoMsg(self,'Informacion',f'Materia se cambio a estado {ActualState} con exito')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = estmate()
    mi_aplicacion.show()
    sys.exit(app.exec_())