from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from Vista.UI_EliminarFacultad import Ui_EliminarFacultad
from eventos import *

class elifacu(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent=None):
        super().__init__(parent)
        self.elifacu = Ui_EliminarFacultad()
        self.elifacu.setupUi(self)
        self.parent = parent
        self.elifacu.btn_buscar.clicked.connect(lambda:self.ObtenerDato())
        self.elifacu.btn_eliminar.clicked.connect(lambda:self.EliminarDatos())


    def EliminarDatos(self):
        codfacultad = int(self.elifacu.txt_codfacultad.text())

        self.QueryForAll      = f"DELETE FROM facultad WHERE (idfacultad = {codfacultad})"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        self.con.commit()
        self.parent.ActualizarFacultad(self.parent.QueryForActive)
        self.elifacu.lbl_nombrefacultad.clear()
        self.elifacu.txt_codfacultad.clear()
        self.elifacu.btn_eliminar.setEnabled(False)
        InfoMsg(self,'Informacion','Facultad eliminada con exito')



    def ObtenerDato(self):
        
        codFacultad = self.elifacu.txt_codfacultad.text()
        codFacultad = int(codFacultad) 
     
        self.QueryForAll      = f"select idfacultad,nombre,siglas from facultad where idfacultad = {codFacultad}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        DatosFacu = self.cur.fetchall()
        
        
       

        if(DatosFacu != []):
            self.elifacu.lbl_nombrefacultad.setText(   DatosFacu[0][1] + " - " + DatosFacu[0][2]      )
            self.elifacu.btn_eliminar.setEnabled(True)
    

        else:
            self.elifacu.lbl_nombrefacultad.setText("No existe dicha facultad" )
            



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = elifacu()
    mi_aplicacion.show()
    sys.exit(app.exec_())