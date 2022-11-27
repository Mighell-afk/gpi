from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from z_modules.conexion import BaseDeDatos

from Vista.Carrera.UI_EliminarCarrera import Ui_EliminarCarrera
from z_modules.eventos import *

class eliminarCarrera(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.eliminarCarrera = Ui_EliminarCarrera()
        self.eliminarCarrera.setupUi(self)
        self.parent=parent

        self.CargarComboBox()

        self.eliminarCarrera.btn_buscar.clicked.connect(lambda:self.ObtenerDatos())

    def CargarComboBox(self):
        sql = "select * from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        listaFacultad = self.cur.fetchall()
        for facultad in listaFacultad():
            datosfacultad = str(facultad[0]) + facultad[1]
            self.eliminarCarrera.cbo_Facultad.addItems(datosfacultad)

    def ObtenerDatos(self):
        codCarrera = self.eliminarCarrera.txt_codcarrera.text()
        codCarrera = int(codCarrera)

        self.QueryForAll = f""
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        DatosCarrera = self.cur.fetchall()

        if(DatosCarrera != []):
            self.eliminarCarrera.lbl_nombreCarrera.setText(DatosCarrera[0][1] + " - " + DatosCarrera[0][2])
            self.eliminarCarrera.btn_eliminar.setEnabled(True)
        else:
            self.eliminarCarrera.lbl_nombreCarrera.setText("No existe dicha carrera")