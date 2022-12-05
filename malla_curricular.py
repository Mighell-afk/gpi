from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from conexion import BaseDeDatos
from Vista.UI_MallaCurricular import Ui_MallaCurricular
from VerMalla import VerMalla
from AnadirMalla import AnadirMalla
from ModificarMalla import ModificarMalla
from EliminarMalla import EliminarMalla
from EstadoMalla import EstadoMalla
import sys

from eventos import *

class malla_curricular(QMainWindow):
    def __init__(self):
        super(malla_curricular, self).__init__()

        self.malla = Ui_MallaCurricular()
        self.malla.setupUi(self)

        self.IDMallaActual = -1

        self.QueryForAll      = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.fecha_inicio from malla_curricular ma inner join carrera ca on ma.idcarrera = ca.idcarrera inner join facultad fa on ma.idfacultad = fa.idfacultad inner join modalidad mo on ma.idmodalidad = mo.idmodalidad"
        self.QueryForActive   = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.fecha_inicio from malla_curricular ma inner join carrera ca on ma.idcarrera = ca.idcarrera inner join facultad fa on ma.idfacultad = fa.idfacultad inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.activo = 1"
        self.QueryForInactive = "select ma.idmalla_curricular, ca.nombre, fa.nombre, mo.descripcion, ma.promocion, ma.fecha_inicio from malla_curricular ma inner join carrera ca on ma.idcarrera = ca.idcarrera inner join facultad fa on ma.idfacultad = fa.idfacultad inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.activo = 0"

        self.ActualizarMallas(self.QueryForActive)

        self.malla.btn_ver_malla.clicked.connect(lambda: self.AbrirVerMalla())
        self.malla.btn_agregar.clicked.connect(lambda:self.AbrirAgregarMalla())
        self.malla.btn_modificar.clicked.connect(lambda:self.AbrirModificarMalla())
        self.malla.btn_eliminar.clicked.connect(lambda: self.AbrirEliminarMalla())
        self.malla.btn_baja.clicked.connect(lambda: self.AbrirEstadoMalla())
        self.malla.table_mallas.cellClicked.connect(lambda:self.ObtenerIDMalla())
        self.malla.btn_filtrar.clicked.connect(lambda:self.FilterPerQuery())

        self.malla.txt_buscar_mallla.textChanged.connect(self.FilterTable)

    def AbrirVerMalla(self):
        if(self.IDMallaActual != -1):
            self.VerMalla = VerMalla(self)
            self.VerMalla.show()
        else:
            WarningMsg(self,'Informacion','Seleccione una malla')

    def AbrirAgregarMalla(self):
        self.AgregarMalla = AnadirMalla(self)
        self.AgregarMalla.show()

    def AbrirModificarMalla(self):
        if(self.IDMallaActual != -1):
            self.ModificarMalla = ModificarMalla(self)
            self.ModificarMalla.show()
        else:
            WarningMsg(self,'Informacion','Seleccione una malla')

    def AbrirEliminarMalla(self):
        self.EliminarMalla = EliminarMalla(self)
        self.EliminarMalla.show()

    def AbrirEstadoMalla(self):
        self.EstadoMalla = EstadoMalla(self)
        self.EstadoMalla.show()

    def FilterPerQuery(self):
        if self.malla.rdb_all.isChecked() == True:
            self.ActualizarMallas(self.QueryForAll)

        elif self.malla.rdb_activo.isChecked() == True:
            self.ActualizarMallas(self.QueryForActive)
            
        elif self.malla.rdb_inactivo.isChecked() == True:
            self.ActualizarMallas(self.QueryForInactive)

    def FilterTable(self):
        for i in range(self.malla.table_mallas.rowCount()):
            for j in range(self.malla.table_mallas.columnCount()):
                item = self.malla.table_mallas.item(i, j).text()
                match = self.malla.txt_buscar_mallla.text().lower() not in item.lower()
                self.malla.table_mallas.setRowHidden(i, match)
                if not match:
                    break

    def ActualizarMallas(self, query):
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
            
    def ObtenerIDMalla(self):
        filaActual = self.malla.table_mallas.currentRow()
        self.IDMallaActual = self.malla.table_mallas.item(filaActual, 0).text()
        
    def closeEvent(self, event: QCloseEvent):
        from main import program
        self.program = program()
        self.program.show()
