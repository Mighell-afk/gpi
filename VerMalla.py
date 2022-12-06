from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos

from Vista.UI_VerMalla import Ui_VerMalla
from VerPrerrequisito import VerPrerrequisito

class VerMalla(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vermalla = Ui_VerMalla()
        self.vermalla.setupUi(self)

        self.parent = parent

        self.idMateriaActual = -1

        self.ObtenerDatosMalla()
        self.ObtenerMaterias()

        self.vermalla.btn_ver_prerrequisito.clicked.connect(lambda: self.AbrirVerPrerrequisito())
        self.vermalla.table_materia.cellClicked.connect(lambda:self.ActualizarIDs())

    def AbrirVerPrerrequisito(self):
        if (self.idMateriaActual != -1):
            self.VerPrerrequisito = VerPrerrequisito(self)
            self.VerPrerrequisito.show()

    def ActualizarIDs(self):
        filaActual = self.vermalla.table_materia.currentRow()
        self.idMateriaActual = self.vermalla.table_materia.item(filaActual, 0).text()

    def ObtenerDatosMalla(self):
        idMalla = int(self.parent.IDMallaActual)

        sql = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.ano_inicio, ma.fecha_inicio, ma.duracion_aproximada from malla_curricular ma "
        sql += "inner join carrera ca on ma.idcarrera = ca.idcarrera "
        sql += "inner join facultad fa on ma.idfacultad = fa.idfacultad "
        sql += f"inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.idmalla_curricular = {idMalla};"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        malla = self.cur.fetchall()

        if malla != []:
            self.vermalla.txt_cod_malla.setText(str(malla[0][0]))
            self.vermalla.txt_carrera.setText(str(malla[0][1]))
            self.vermalla.txt_facultad.setText(str(malla[0][2]))
            self.vermalla.txt_modalidad.setText(str(malla[0][3]))
            self.vermalla.txt_promocion.setText(str(malla[0][4]))
            self.vermalla.txt_ano_inicio.setText(str(malla[0][5]))
            self.vermalla.txt_fecha_inicio.setText(str(malla[0][6]))
            self.vermalla.txt_duracion.setText(str(malla[0][7]))

    def ObtenerMaterias(self):
        idMalla = int(self.parent.IDMallaActual)

        sql = "select det.idmateria, ma.nombre, fa.nombre, det.creditos_teoricos, det.creditos_practicos,  det.cantidad_horas from detalle_malla det "
        sql += "inner join materia ma on det.idmateria = ma.idmateria "
        sql += f"inner join facultad fa on ma.idfacultad = fa.idfacultad where det.idmalla_curricular = {idMalla};"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        materias = self.cur.fetchall()

        header = ["Codigo","Materia","Facultad","Creditos Teoricos","Creditos Practicos","Cant. Horas"]

        filas = len(materias)
        columnas = len(header)

        self.vermalla.table_materia.setRowCount(filas)
        self.vermalla.table_materia.setColumnCount(columnas)

        self.vermalla.table_materia.setHorizontalHeaderLabels(header)

        fila = 0
        for materia in materias:
            listaDatos = [materia[0],materia[1],materia[2],materia[3],materia[4],materia[5]]
            for columna in range(columnas):
                celda = QTableWidgetItem(str(listaDatos[columna]))
                self.vermalla.table_materia.setItem(fila,columna,celda)
            fila += 1


# select det.idmateria, ma.idfacultad,  ma.nombre, fa.nombre, det.creditos_teoricos, det.creditos_practicos,  det.cantidad_horas from detalle_malla det
# inner join materia ma on det.idmateria = ma.idmateria
# inner join facultad fa on ma.idfacultad = fa.idfacultad where det.idmalla_curricular = {};