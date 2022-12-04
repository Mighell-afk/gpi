from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from conexion import BaseDeDatos
from Vista.UI_MallaCurricular import Ui_MallaCurricular
from AnadirMalla import AnadirMalla
from EliminarMalla import EliminarMalla
import sys

class malla_curricular(QMainWindow):
    def __init__(self):
        super(malla_curricular, self).__init__()

        self.malla = Ui_MallaCurricular()
        self.malla.setupUi(self)

        self.QueryForAll      = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.fecha_inicio from malla_curricular ma inner join carrera ca on ma.idcarrera = ca.idcarrera inner join facultad fa on ma.idfacultad = fa.idfacultad inner join modalidad mo on ma.idmodalidad = mo.idmodalidad"
        self.QueryForActive   = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.fecha_inicio from malla_curricular ma inner join carrera ca on ma.idcarrera = ca.idcarrera inner join facultad fa on ma.idfacultad = fa.idfacultad inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.activo = 1"
        self.QueryForInactive = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.fecha_inicio from malla_curricular ma inner join carrera ca on ma.idcarrera = ca.idcarrera inner join facultad fa on ma.idfacultad = fa.idfacultad inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.activo = 0"

        self.ActualizarMallas(self.QueryForActive)

        self.malla.btn_agregar.clicked.connect(lambda:self.AbrirAgregarMalla())
        self.malla.btn_eliminar.clicked.connect(lambda: self.AbrirEliminarMalla())

    def AbrirAgregarMalla(self):
        self.AgregarMalla = AnadirMalla(self)
        self.AgregarMalla.show()

    def AbrirEliminarMalla(self):
        self.EliminarMalla = EliminarMalla(self)
        self.EliminarMalla.show()

    def ActualizarMallas(self, query):
        self.malla.cbo_filterMalla.setCurrentIndex(-1)
        header=["Codigo", "Carrera", "Facultad", "Modalidad", "Promocion", "Fecha Inicio"]

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(query)
        mallas = self.cur.fetchall()

        filas = len(mallas)
        columnas = len(header)

        self.malla.table_mallas.setColumnCount(columnas)
        self.malla.table_mallas.setRowCount(filas)

        self.malla.table_mallas.setHorizontalHeaderLabels(header)

        fila = 0

        for malla in mallas:
            listaDatos = [str(malla[0]), malla[1], malla[2], malla[3], str(malla[4]), str(malla[5])]
            for columna in range(columnas):
                celda = QTableWidgetItem(listaDatos[columna])
                self.malla.table_mallas.setItem(fila, columna, celda)
            fila+=1

        for indice, ancho in enumerate((100,400,400,120,100,100),start=0):
            self.malla.table_mallas.setColumnWidth(indice,ancho)
            
    def closeEvent(self, event: QCloseEvent):
        from main import program
        self.program = program()
        self.program.show()
