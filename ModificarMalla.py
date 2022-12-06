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

class ModificarMalla(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.modificarmalla = UI_AgregarMalla()
        self.modificarmalla.setupUi(self)

        self.modificarmalla.label.setText("Modificar Malla")
        self.modificarmalla.txt_cod_malla.setEnabled(False)
        self.modificarmalla.cbo_facultad.setEnabled(False)
        self.modificarmalla.cbo_carrera.setEnabled(False)

        self.parent = parent

        self.ListaMaterias = []
        self.filaActual = -1

        self.CargarFacultad()
        self.CargarCarrera()
        self.CargarModalidad()
        
        self.ObtenerDatosMalla()
        self.ObtenerDatosMateria()
        self.ActualizarListaMaterias()

        self.modificarmalla.btn_anadir_materia.clicked.connect(lambda:self.AbrirAgregarMateria())
        self.modificarmalla.btn_eliminar_materia.clicked.connect(lambda:self.EliminarMateria())
        self.modificarmalla.btn_anadir_prerrequisito.clicked.connect(lambda:self.AbrirAgregarPrerrequisitos())
        self.modificarmalla.btn_guardar_malla.clicked.connect(lambda:self.GuardarMalla())
        self.modificarmalla.table_materia.cellClicked.connect(lambda:self.ActualizarIDs())

    def GuardarMalla(self):
        idMalla = int(self.modificarmalla.txt_cod_malla.text())
        idModalidad = int(self.modificarmalla.cbo_modalidad.currentData())
        promocion = int(self.modificarmalla.txt_promocion.text())
        anoInicio = int(self.modificarmalla.txt_ano_inicio.text())
        fechaInicio = str(self.modificarmalla.date_fecha_inicio.text())
        duracionAproximada = int(self.modificarmalla.txt_duracion.text())

        self.EliminarDetalles()

        sql = "UPDATE `UAAMallaCurricular`.`malla_curricular`"
        sql += f"SET `idmodalidad` = {idModalidad}, `promocion` = {promocion}, `ano_inicio` = {anoInicio}, `fecha_inicio` = STR_TO_DATE(\"{fechaInicio}\",\"%d/%m/%Y\"), `duracion_aproximada` = {duracionAproximada} "
        sql += f"WHERE `idmalla_curricular` = {idMalla};"

        self.cur.execute(sql)
        self.con.commit()

        for materia in self.ListaMaterias:
            idMateria = materia["Materia"]["IDMateria"]
            creditosTeoricos = materia["Materia"]["Teoricos"]
            creditosPracticos = materia["Materia"]["Practicos"]
            cantidadHoras = materia["Materia"]["Horas"]

            sql = "INSERT INTO `detalle_malla` (`idmalla_curricular`,`idmateria`,`creditos_teoricos`,`creditos_practicos`,`cantidad_horas`)"         
            sql += f"VALUES ({idMalla},{idMateria},{creditosTeoricos},{creditosPracticos},{cantidadHoras});"   

            self.cur.execute(sql)
            self.con.commit()

            if (len(materia["Prerrequisitos"]) > 0):
                for prerrequisito in materia["Prerrequisitos"]:
                    idMateriaPrerrequisito = prerrequisito["IDMateria"]

                    sql = "INSERT INTO `detalle_prerrequisito`(`materia_idmateria`,`detalle_idmateria`,`detalle_idmalla`)"
                    sql += f"VALUES ({idMateriaPrerrequisito},{idMateria},{idMalla});"

                    self.cur.execute(sql)
                    self.con.commit()
                    
        InfoMsg(self,'Informacion','Malla Cargada con exito')
        self.parent.ActualizarMallas(self.parent.QueryForActive)
        self.close()


    def EliminarDetalles(self):
        idMalla = int(self.modificarmalla.txt_cod_malla.text())
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        try:
            sql = f"delete from detalle_prerrequisito where detalle_idmalla = {idMalla}"
            
            self.cur = self.con.cursor()
            self.cur.execute(sql)

            sql = f"delete from detalle_malla where idmalla_curricular = {idMalla}"
            self.cur = self.con.cursor()
            self.cur.execute(sql)
            
            self.con.commit()

        except:
            print("jajaj")
            self.con.rollback()


    def ActualizarIDs(self):
        self.filaActual = self.modificarmalla.table_materia.currentRow()
        self.idMateriaActual = self.modificarmalla.table_materia.item(self.filaActual, 0).text()

    def AbrirAgregarMateria(self):
        self.AgregarMateria = AnadirMateriaMalla(self)
        self.AgregarMateria.show()

    def AbrirAgregarPrerrequisitos(self):
        if self.filaActual != -1:
            self.AgregarPrerrequisito = AnadirPrerrequisito(self)
            self.AgregarPrerrequisito.show()

    def EliminarMateria(self):
        filaEliminar = self.filaActual
        if filaEliminar != -1:
            del self.ListaMaterias[filaEliminar]
            self.ActualizarListaMaterias()
            self.filaActual = -1

    def CargarFacultad(self):
        sql = "select idfacultad,nombre from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        facultades = self.cur.fetchall()

        for facultad in facultades:
            self.modificarmalla.cbo_facultad.addItem(facultad[1],str(facultad[0]))

    def CargarCarrera(self):
        sql = f"select idcarrera,nombre from carrera"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        carreras = self.cur.fetchall()

        for carrera in carreras:
            self.modificarmalla.cbo_carrera.addItem(carrera[1],str(carrera[0]))

        self.modificarmalla.cbo_carrera.setCurrentIndex(-1)

    def CargarModalidad(self):
        sql = f"select idmodalidad, descripcion from modalidad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        modalidades = self.cur.fetchall()

        for modalidad in modalidades:
            self.modificarmalla.cbo_modalidad.addItem(modalidad[1], str(modalidad[0]))

    def ObtenerDatosMalla(self):
        idMalla = int(self.parent.IDMallaActual)

        sql = "select ma.idmalla_curricular, ca.idcarrera, fa.idfacultad, mo.idmodalidad, ma.promocion, ma.ano_inicio, ma.fecha_inicio, ma.duracion_aproximada from malla_curricular ma "
        sql += "inner join carrera ca on ma.idcarrera = ca.idcarrera "
        sql += "inner join facultad fa on ma.idfacultad = fa.idfacultad "
        sql += f"inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.idmalla_curricular = {idMalla};"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        malla = self.cur.fetchall()

        if malla != []:
            indexcarrera = self.modificarmalla.cbo_carrera.findData(malla[0][1])
            indexfacultad = self.modificarmalla.cbo_facultad.findData(malla[0][2])
            indexmodalidad = self.modificarmalla.cbo_modalidad.findData((malla[0][3]))
            self.modificarmalla.txt_cod_malla.setText(str(malla[0][0]))
            self.modificarmalla.cbo_carrera.setCurrentIndex(indexcarrera)
            self.modificarmalla.cbo_facultad.setCurrentIndex(indexfacultad)
            self.modificarmalla.cbo_modalidad.setCurrentIndex(indexmodalidad)
            self.modificarmalla.txt_promocion.setText(str(malla[0][4]))
            self.modificarmalla.txt_ano_inicio.setText(str(malla[0][5]))
            self.modificarmalla.date_fecha_inicio.setDate(malla[0][6])
            self.modificarmalla.txt_duracion.setText(str(malla[0][7]))

    def ObtenerDatosMateria(self):
        idMalla = int(self.parent.IDMallaActual)

        sql = "select det.idmateria, ma.idfacultad, ma.nombre, fa.nombre, det.creditos_teoricos, det.creditos_practicos, det.cantidad_horas from detalle_malla det "
        sql += "inner join materia ma on det.idmateria = ma.idmateria "
        sql += f"inner join facultad fa on ma.idfacultad = fa.idfacultad where det.idmalla_curricular = {idMalla};"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        materias = self.cur.fetchall()

        currentIndex = 0
        if materias != []:
            for materia in materias:
                idMateria = str(materia[0])
                idFacultad = str(materia[1])
                NombreMateria = materia[2]
                NombreFacultad = materia[3]
                creditosTeoricos = str(materia[4])
                creditosPracticos = str(materia[5])
                cantidadHoras = str(materia[6])
                diccionario = {"Materia":{"IDMateria": idMateria, "IDFacultad":idFacultad,"NombreMateria":NombreMateria,"NombreFacultad":NombreFacultad, "Teoricos":creditosTeoricos, "Practicos":creditosPracticos, "Horas": cantidadHoras} , "Prerrequisitos":[]}
                self.ListaMaterias.append(diccionario)

                sql = "select ma.idmateria, ma.idfacultad, ma.nombre, fa.nombre from detalle_prerrequisito pre "
                sql += "inner join materia ma on pre.materia_idmateria = ma.idmateria "
                sql += "inner join facultad fa on ma.idfacultad = fa.idfacultad "
                sql += f"where pre.detalle_idmateria = {idMateria} and pre.detalle_idmalla = {idMalla}"

                self.connect = BaseDeDatos()
                self.con = self.connect.con
                self.cur = self.con.cursor()
                self.cur.execute(sql)
                prerrequisitos = self.cur.fetchall()

                if (prerrequisitos != []):
                    for prerrequisito in prerrequisitos:
                        preIdMateria = str(prerrequisito[0])
                        preidFacultad = str(prerrequisito[1])
                        preNombreMateria = prerrequisito[2]
                        preNombreFacultad = prerrequisito[3]
                        diccionario = {"IDMateria": preIdMateria, "IDFacultad":preidFacultad,"NombreMateria":preNombreMateria,"NombreFacultad":preNombreFacultad}
                        self.ListaMaterias[currentIndex]["Prerrequisitos"].append(diccionario)
                
                currentIndex += 1
        else:
            InfoMsg(self,'Informacion','Esta malla no tiene materias asignadas')

    def ActualizarListaMaterias(self):
        
        header = ["Codigo","Materia","Facultad"]

        filas = len(self.ListaMaterias)
        columnas = len(header)

        self.modificarmalla.table_materia.setColumnCount(columnas)
        self.modificarmalla.table_materia.setRowCount(filas)

        self.modificarmalla.table_materia.setHorizontalHeaderLabels(header)

        fila = 0
        for materia in self.ListaMaterias:
            idMateria = materia["Materia"]["IDMateria"]
            nombreMateria = materia["Materia"]["NombreMateria"]
            nombrefacultad = materia["Materia"]["NombreFacultad"]
            listaDatos = [idMateria,nombreMateria,nombrefacultad]
            for columna in range(columnas):
                celda = QTableWidgetItem(listaDatos[columna])
                self.modificarmalla.table_materia.setItem(fila, columna, celda)
            fila+=1

        for indice, ancho in enumerate((170,400,400),start=0):
            self.modificarmalla.table_materia.setColumnWidth(indice,ancho)
