from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos

from Vista.UI_VerPrerrequisito import Ui_VerPrerrequisito

class VerPrerrequisito(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.verprerrequisito = Ui_VerPrerrequisito()
        self.verprerrequisito.setupUi(self)

        self.parent = parent

        self.CargarPrerrequisitos()

    def CargarPrerrequisitos(self):

        idMateria = int(self.parent.idMateriaActual)
        idMalla = int(self.parent.parent.IDMallaActual)

        sql = "select pre.materia_idmateria, ma.nombre, fa.nombre from detalle_prerrequisito pre "
        sql += "inner join materia ma on pre.materia_idmateria = ma.idmateria "
        sql += "inner join facultad fa on ma.idfacultad = fa.idfacultad "
        sql += f"where pre.detalle_idmateria = {idMateria} and pre.detalle_idmalla = {idMalla}"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        prerrequisitos = self.cur.fetchall()

        header = ["Codigo","Materia","Facultad"]

        filas = len(prerrequisitos)
        columnas = len(header)

        self.verprerrequisito.table_prerrequisito.setRowCount(filas)
        self.verprerrequisito.table_prerrequisito.setColumnCount(columnas)

        self.verprerrequisito.table_prerrequisito.setHorizontalHeaderLabels(header)

        fila = 0
        for prerrequisito in prerrequisitos:
            listaDatos = [prerrequisito[0],prerrequisito[1],prerrequisito[2]]
            for columna in range(columnas):
                celda = QTableWidgetItem(str(listaDatos[columna]))
                self.verprerrequisito.table_prerrequisito.setItem(fila,columna,celda)
            fila += 1


# select pre.materia_idmateria, ma.nombre, fa.nombre from detalle_prerrequisito pre
# inner join materia ma on pre.materia_idmateria = ma.idmateria
# inner join facultad fa on ma.idfacultad = fa.idfacultad