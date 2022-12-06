from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from eventos import *
from Vista.UI_AgregarPrerrequisito import Ui_CargarPrerrequisito

class AnadirPrerrequisito(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.UI_AgregarPrerrequisito = Ui_CargarPrerrequisito()
        self.UI_AgregarPrerrequisito.setupUi(self)

        self.parent=parent

        self.ActualizarListaPrerrequisito()
        self.CargarFacultad()
        self.UI_AgregarPrerrequisito.cbo_facultad.setCurrentIndex(-1)
        self.UI_AgregarPrerrequisito.cbo_facultad.currentIndexChanged.connect(lambda:self.CargarMateria())

        self.UI_AgregarPrerrequisito.btn_Anadir.clicked.connect(lambda:self.AnadirPrerrequisito())
        self.UI_AgregarPrerrequisito.btn_Eliminar.clicked.connect(lambda:self.EliminarPrerrequisito())
        
    def AnadirPrerrequisito(self):
        filaActual = self.parent.filaActual

        idMateria = self.UI_AgregarPrerrequisito.cbo_materia.currentData()
        idFacultad = self.UI_AgregarPrerrequisito.cbo_facultad.currentData()
        NombreMateria = self.UI_AgregarPrerrequisito.cbo_materia.currentText()
        nombreFacultad = self.UI_AgregarPrerrequisito.cbo_facultad.currentText()

        if (idMateria != None and idFacultad != None):
            diccionario = {"IDMateria": idMateria, "IDFacultad":idFacultad,"NombreMateria":NombreMateria,"NombreFacultad":nombreFacultad}
            self.parent.ListaMaterias[filaActual]["Prerrequisitos"].append(diccionario)
            self.ActualizarListaPrerrequisito()

    def EliminarPrerrequisito(self):
        filaActual = self.parent.filaActual
        filaEliminar = self.filaActual = self.UI_AgregarPrerrequisito.table_prerrequisito.currentRow()
        if filaActual != -1 and filaEliminar != -1:
            filaEliminar = self.filaActual = self.UI_AgregarPrerrequisito.table_prerrequisito.currentRow()
            del self.parent.ListaMaterias[filaActual]["Prerrequisitos"][filaEliminar]
            self.ActualizarListaPrerrequisito()

    def ActualizarListaPrerrequisito(self):
        
        filaActual = self.parent.filaActual

        header = ["Codigo","Materia","Facultad"]

        filas = len(self.parent.ListaMaterias[filaActual]["Prerrequisitos"])
        columnas = len(header)

        self.UI_AgregarPrerrequisito.table_prerrequisito.setColumnCount(columnas)
        self.UI_AgregarPrerrequisito.table_prerrequisito.setRowCount(filas)

        self.UI_AgregarPrerrequisito.table_prerrequisito.setHorizontalHeaderLabels(header)

        fila = 0
        for prerrequisito in self.parent.ListaMaterias[filaActual]["Prerrequisitos"]:
            idMateria = prerrequisito["IDMateria"]
            nombreMateria = prerrequisito["NombreMateria"]
            nombrefacultad = prerrequisito["NombreFacultad"]
            lista = [idMateria,nombreMateria,nombrefacultad]
            for columna in range(columnas):
                celda = QTableWidgetItem(lista[columna])
                self.UI_AgregarPrerrequisito.table_prerrequisito.setItem(fila, columna, celda)
            fila+=1
            

    def CargarFacultad(self):
        sql = "select idfacultad,nombre from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        facultades = self.cur.fetchall()

        for facultad in facultades:
            self.UI_AgregarPrerrequisito.cbo_facultad.addItem(facultad[1],str(facultad[0]))

    def CargarMateria(self):
        self.UI_AgregarPrerrequisito.cbo_materia.clear()
        idfacultad = self.UI_AgregarPrerrequisito.cbo_facultad.currentData()
        sql = f"select idmateria, nombre from materia where idfacultad = {idfacultad}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        materias = self.cur.fetchall()

        for materia in materias:
            self.UI_AgregarPrerrequisito.cbo_materia.addItem(materia[1], str(materia[0]))

        self.UI_AgregarPrerrequisito.cbo_materia.setCurrentIndex(-1)
    
    # def SeleccionarMateria(self):
    #     print(filaActual, self.parent.idMateriaActual)