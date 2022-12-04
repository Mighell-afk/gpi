from datetime import datetime
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from conexion import BaseDeDatos
from eventos import *
from Vista.UI_AgregarMalla import UI_AgregarMalla
from AnadirMateriaMalla import AnadirMateriaMalla
from AnadirPrerrequisito import AnadirPrerrequisito

import sys

class AnadirMalla(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.UI_AgregarMalla = UI_AgregarMalla()
        self.UI_AgregarMalla.setupUi(self)

        self.parent=parent
        self.ListaMaterias = []
        self.filaActual = -1

        self.CargarFacultad()
        self.CargarModalidad()
        self.ActualizarListaMaterias()

        self.UI_AgregarMalla.cbo_facultad.setCurrentIndex(-1)
        self.UI_AgregarMalla.cbo_modalidad.setCurrentIndex(-1)
        self.UI_AgregarMalla.date_fecha_inicio.setDate(datetime.now())

        self.UI_AgregarMalla.cbo_facultad.currentIndexChanged.connect(lambda:self.CargarCarrera())
        self.UI_AgregarMalla.btn_anadir_materia.clicked.connect(lambda:self.AbrirAgregarMateria())
        self.UI_AgregarMalla.btn_eliminar_materia.clicked.connect(lambda:self.EliminarMateria())
        self.UI_AgregarMalla.btn_anadir_prerrequisito.clicked.connect(lambda:self.AbrirAgregarPrerrequisitos())
        self.UI_AgregarMalla.btn_guardar_malla.clicked.connect(lambda:self.GuardarMalla())
        self.UI_AgregarMalla.table_materia.cellClicked.connect(lambda:self.ActualizarIDs())

    def ActualizarIDs(self):
        self.filaActual = self.UI_AgregarMalla.table_materia.currentRow()
        self.idMateriaActual = self.UI_AgregarMalla.table_materia.item(self.filaActual, 0).text()

    def AbrirAgregarMateria(self):
        self.AgregarMateria = AnadirMateriaMalla(self)
        self.AgregarMateria.show()

    def EliminarMateria(self):
        filaEliminar = self.filaActual
        if filaEliminar != -1:
            del self.ListaMaterias[filaEliminar]
            self.ActualizarListaMaterias()
            self.filaActual = -1

    def GuardarMalla(self):
        codMalla = int(self.UI_AgregarMalla.txt_cod_malla.text())
        idCarrera = self.UI_AgregarMalla.cbo_carrera.currentData()
        idFacultad = self.UI_AgregarMalla.cbo_facultad.currentData()
        idModalidad = self.UI_AgregarMalla.cbo_modalidad.currentData()
        promocion = int(self.UI_AgregarMalla.txt_promocion.text())
        anoInicio = int(self.UI_AgregarMalla.txt_ano_inicio.text())
        fechaInicio = self.UI_AgregarMalla.date_fecha_inicio.text()
        duracionAproximada = int(self.UI_AgregarMalla.txt_duracion.text())

        sql = "INSERT INTO `malla_curricular` (`idmalla_curricular`, `idcarrera`, `idfacultad`, `idmodalidad`, `promocion`, `ano_inicio`, `fecha_inicio`, `duracion_aproximada`)"
        sql += f"VALUES ({codMalla},{idCarrera},{idFacultad},{idModalidad},{promocion},{anoInicio},STR_TO_DATE(\"{fechaInicio}\",\"%d/%m/%Y\"),{duracionAproximada});"

        self.cur.execute(sql)
        self.con.commit()

        for materia in self.ListaMaterias:
            idMateria = materia["Materia"]["IDMateria"]
            creditosTeoricos = materia["Materia"]["Teoricos"]
            creditosPracticos = materia["Materia"]["Practicos"]
            cantidadHoras = materia["Materia"]["Horas"]

            sql = "INSERT INTO `detalle_malla` (`idmalla_curricular`,`idmateria`,`creditos_teoricos`,`creditos_practicos`,`cantidad_horas`)"         
            sql += f"VALUES ({codMalla},{idMateria},{creditosTeoricos},{creditosPracticos},{cantidadHoras});"   

            self.cur.execute(sql)
            self.con.commit()

            if (len(materia["Prerrequisitos"]) > 0):
                for prerrequisito in materia["Prerrequisitos"]:
                    idMateriaPrerrequisito = prerrequisito["IDMateria"]

                    sql = "INSERT INTO `detalle_prerrequisito`(`materia_idmateria`,`detalle_idmateria`,`detalle_idmalla`)"
                    sql += f"VALUES ({idMateriaPrerrequisito},{idMateria},{codMalla});"

                    self.cur.execute(sql)
                    self.con.commit()
                    
        InfoMsg(self,'Informacion','Malla Cargada con exito')
        self.parent.ActualizarMallas()
        self.close()

    def AbrirAgregarPrerrequisitos(self):
        if self.filaActual != -1:
            self.AgregarPrerrequisito = AnadirPrerrequisito(self)
            self.AgregarPrerrequisito.show()

    def CargarFacultad(self):
        sql = "select idfacultad,nombre from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        facultades = self.cur.fetchall()

        for facultad in facultades:
            self.UI_AgregarMalla.cbo_facultad.addItem(facultad[1],str(facultad[0]))

    def CargarCarrera(self):
        self.UI_AgregarMalla.cbo_carrera.clear()
        idfacultad = self.UI_AgregarMalla.cbo_facultad.currentData()
        sql = f"select idcarrera,nombre from carrera where idfacultad = {idfacultad}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        carreras = self.cur.fetchall()

        for carrera in carreras:
            self.UI_AgregarMalla.cbo_carrera.addItem(carrera[1],str(carrera[0]))

        self.UI_AgregarMalla.cbo_carrera.setCurrentIndex(-1)

    def CargarModalidad(self):
        sql = f"select idmodalidad, descripcion from modalidad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        modalidades = self.cur.fetchall()

        for modalidad in modalidades:
            self.UI_AgregarMalla.cbo_modalidad.addItem(modalidad[1], str(modalidad[0]))

    def ActualizarListaMaterias(self):
        
        header = ["Codigo","Materia","Facultad"]

        filas = len(self.ListaMaterias)
        columnas = len(header)

        self.UI_AgregarMalla.table_materia.setColumnCount(columnas)
        self.UI_AgregarMalla.table_materia.setRowCount(filas)

        self.UI_AgregarMalla.table_materia.setHorizontalHeaderLabels(header)

        fila = 0
        for materia in self.ListaMaterias:
            idMateria = materia["Materia"]["IDMateria"]
            nombreMateria = materia["Materia"]["NombreMateria"]
            nombrefacultad = materia["Materia"]["NombreFacultad"]
            listaDatos = [idMateria,nombreMateria,nombrefacultad]
            for columna in range(columnas):
                celda = QTableWidgetItem(listaDatos[columna])
                self.UI_AgregarMalla.table_materia.setItem(fila, columna, celda)
            fila+=1

        for indice, ancho in enumerate((170,400,400),start=0):
            self.UI_AgregarMalla.table_materia.setColumnWidth(indice,ancho)
