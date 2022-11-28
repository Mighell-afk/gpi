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

        self.idfacultad = 0

        self.CargarComboBox()

        self.eliminarCarrera.btn_buscar.clicked.connect(lambda:self.ObtenerDatos())

        self.eliminarCarrera.cbo_Facultad.currentIndexChanged.connect(lambda:self.ObtenerID())

    def ObtenerID(self):
        textfacultad = self.eliminarCarrera.cbo_Facultad.currentText()
        textfacultad = textfacultad.split("-")
        idfacultad = int(textfacultad[0])
        self.idfacultad = idfacultad

    def CargarComboBox(self):
        sql = "select idfacultad,nombre from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        datosfacultad = self.cur.fetchall()
        listafacultad = []

        for facultad in datosfacultad:
            listafacultad.append(f"{facultad[0]} - {facultad[1]}")

        self.eliminarCarrera.cbo_Facultad.addItems(listafacultad)
        self.eliminarCarrera.cbo_Facultad.setCurrentIndex(-1)

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