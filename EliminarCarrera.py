from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos

from Vista.UI_EliminarCarrera import Ui_EliminarCarrera
from eventos import *

class eliminarCarrera(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.eliminarCarrera = Ui_EliminarCarrera()
        self.eliminarCarrera.setupUi(self)
        self.parent=parent

        self.idfacultad = 0

        self.CargarComboBox()

        self.eliminarCarrera.btn_buscar.clicked.connect(lambda: self.ObtenerDatos())
        self.eliminarCarrera.btn_eliminar.clicked.connect(lambda: self.EliminarCarrera())


    def CargarComboBox(self):
        sql = "select idfacultad,nombre from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        datosfacultad = self.cur.fetchall()

        for facultad in datosfacultad:
            idfacultad = facultad[0]
            nombreFacultad = facultad[1]
            self.eliminarCarrera.cbo_Facultad.addItem(nombreFacultad,str(idfacultad))

        self.eliminarCarrera.cbo_Facultad.setCurrentIndex(-1)

    def ObtenerDatos(self):
        idCarrera = self.eliminarCarrera.txt_codcarrera.text()
        idCarrera = int(idCarrera)

        idFacultad = self.eliminarCarrera.cbo_Facultad.currentData()

        self.QueryForAll = f"select * from carrera where idfacultad = {idFacultad} and idcarrera = {idCarrera}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        DatosCarrera = self.cur.fetchall()

        if(DatosCarrera != []):
            self.eliminarCarrera.lbl_nombreCarrera.setText(f"{DatosCarrera[0][1]} - {DatosCarrera[0][2]}")
            self.eliminarCarrera.btn_eliminar.setEnabled(True)
        else:
            self.eliminarCarrera.lbl_nombreCarrera.setText("No existe dicha carrera")

    def EliminarCarrera(self):
        idCarrera = self.eliminarCarrera.txt_codcarrera.text()
        idCarrera = int(idCarrera)
        idFacultad = self.eliminarCarrera.cbo_Facultad.currentData()
        self.QueryForAll = f"delete from carrera where idfacultad = {idFacultad} and idcarrera = {idCarrera}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryForAll)
        self.con.commit()
        self.LimpiarCampos()

    def LimpiarCampos(self):
        self.eliminarCarrera.lbl_nombreCarrera.clear()
        self.eliminarCarrera.txt_codcarrera.clear()
        self.eliminarCarrera.cbo_Facultad.setCurrentIndex(-1)