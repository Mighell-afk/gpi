from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from Vista.ui_estadoFacu import Ui_EstadoFacultad
from conexion import BaseDeDatos
from eventos import *
class estfacu(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent = None):
        super().__init__(parent)
        self.estfacu = Ui_EstadoFacultad()
        self.estfacu.setupUi(self)
        self.parent = parent
        self.estfacu.btn_buscar.clicked.connect(lambda:self.ObtenerDato())
        self.estfacu.btn_cambiarEstado.clicked.connect(lambda:self.CambiarEstado())

    def ObtenerDato(self):
        global DatosFacu
        codFacultad = self.estfacu.txt_codfacultad.text()
    
        if self.ValidarDatos():
            self.QueryForAll      = f"select * from facultad where idfacultad = {int(codFacultad)}"
            self.connect = BaseDeDatos()
            self.con = self.connect.con
            self.cur = self.con.cursor()
            self.cur.execute(self.QueryForAll)
            DatosFacu = self.cur.fetchall()
            if(DatosFacu != []):
                if DatosFacu[0][3] == 1:
                    EstActual =  "Activo" 
                else:
                    EstActual = "Inactivo"

                self.estfacu.lbl_nombrefacultad.setText(DatosFacu[0][1] + " - " + EstActual )
                self.estfacu.btn_cambiarEstado.setEnabled(True)
            else:
                WarningMsg(self,"Atencion","No existe facultad con ese codigo")    

    def ValidarDatos(self):
        codFacultad = self.estfacu.txt_codfacultad.text()
    
        if not codFacultad.isnumeric():
            WarningMsg(self,"Atencion","Ingrese un numero en el codigo de Facultad")    
            return False
        if codFacultad == "":
            WarningMsg(self,"Atencion","Ingrese un numero en el codigo de Facultad")    
            return False
        
        return True
            

    def CambiarEstado(self):
        codFacultad = self.estfacu.txt_codfacultad.text()
        if DatosFacu[0][3]:
            NewState = 0
        else:
            NewState = 1
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(f"update facultad SET activo ={NewState} WHERE idfacultad = '{codFacultad}'")
        self.con.commit()
        self.estfacu.btn_cambiarEstado.setEnabled(False)
        self.estfacu.txt_codfacultad.clear()
        self.estfacu.lbl_nombrefacultad.clear()
        self.parent.ActualizarFacultad(self.parent.QueryForActive)
        if NewState:
            ActualState = "Activo"
        else:
            ActualState = "Inactivo"
        InfoMsg(self,'Informacion',f'Facultad se cambio a estado {ActualState} con exito')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = estfacu()
    mi_aplicacion.show()
    sys.exit(app.exec_())