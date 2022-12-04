from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from Vista.ui_eliminarMateria import Ui_EliminarMateria
from eventos import *

class EliminarMateria(QtWidgets.QMainWindow):
   
   
    def __init__(self,parent=None):
        super().__init__(parent)
        self.elimate = Ui_EliminarMateria()
        self.elimate.setupUi(self)
        self.parent = parent

        self.elimate.btn_buscar.clicked.connect(lambda:self.ObtenerDato())
        self.elimate.btn_eliminar.clicked.connect(lambda:self.EliminarDatos())



    def EliminarDatos(self):
        codMateria = int(self.elimate.txt_codmateria.text())

        self.QueryForAll      = f"DELETE FROM Materia WHERE (idMateria = {codMateria})"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        self.con.commit()
        self.parent.ActualizarMateria(self.parent.QueryForActive)
        self.elimate.lbl_nombremateria.clear()
        self.elimate.txt_codmateria.clear()
        self.elimate.btn_eliminar.setEnabled(False)
        InfoMsg(self,'Informacion','Materia eliminada con exito')



    def ObtenerDato(self):
        
        codMateria = int(self.elimate.txt_codmateria.text())
     
        self.QueryForAll      = f"select idMateria,nombre from Materia where idMateria = {codMateria}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        DatosMate = self.cur.fetchall()
        
        if(DatosMate != []):
            self.elimate.lbl_nombremateria.setText(   DatosMate[0][1])
            self.elimate.btn_eliminar.setEnabled(True)
        else:
            self.elimate.lbl_nombremateria.setText("No existe dicha Materia" )
            





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = EliminarMateria()
    mi_aplicacion.show()
    sys.exit(app.exec_())