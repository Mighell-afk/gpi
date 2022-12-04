from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from eventos import *
from Vista.UI_AgregarMateriaMalla import Ui_AnadirMateria

class AnadirMateriaMalla(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.UI_AgregarMateriaMalla = Ui_AnadirMateria()
        self.UI_AgregarMateriaMalla.setupUi(self)
        
        self.parent=parent

        self.CargarFacultad()
        self.UI_AgregarMateriaMalla.cbo_facultad.setCurrentIndex(-1)
        self.UI_AgregarMateriaMalla.cbo_facultad.currentIndexChanged.connect(lambda:self.CargarMateria())

        self.UI_AgregarMateriaMalla.btn_Anadir.clicked.connect(lambda:self.AñadirMateria())

    def CargarFacultad(self):
        sql = "select idfacultad,nombre from facultad"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        facultades = self.cur.fetchall()

        for facultad in facultades:
            self.UI_AgregarMateriaMalla.cbo_facultad.addItem(facultad[1],str(facultad[0]))

    def CargarMateria(self):
        self.UI_AgregarMateriaMalla.cbo_materia.clear()
        idfacultad = self.UI_AgregarMateriaMalla.cbo_facultad.currentData()
        sql = f"select idmateria, nombre from materia where idfacultad = {idfacultad}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        materias = self.cur.fetchall()

        for materia in materias:
            self.UI_AgregarMateriaMalla.cbo_materia.addItem(materia[1], str(materia[0]))

        self.UI_AgregarMateriaMalla.cbo_materia.setCurrentIndex(-1)

    def AñadirMateria(self):
        idMateria = self.UI_AgregarMateriaMalla.cbo_materia.currentData()
        idFacultad = self.UI_AgregarMateriaMalla.cbo_facultad.currentData()
        NombreMateria = self.UI_AgregarMateriaMalla.cbo_materia.currentText()
        nombreFacultad = self.UI_AgregarMateriaMalla.cbo_facultad.currentText()
        creditosTeoricos = self.UI_AgregarMateriaMalla.txt_creditos_teoricos.text()
        creditosPracticos = self.UI_AgregarMateriaMalla.txt_creditos_practicos.text()
        cantidadHoras = self.UI_AgregarMateriaMalla.txt_cantidad_horas.text()


        if (idMateria != None and idFacultad != None and creditosTeoricos != "" and creditosPracticos != ""):
            diccionario = {"Materia":{"IDMateria": idMateria, "IDFacultad":idFacultad,"NombreMateria":NombreMateria,"NombreFacultad":nombreFacultad, "Teoricos":creditosTeoricos, "Practicos":creditosPracticos, "Horas": cantidadHoras} , "Prerrequisitos":[]}
            self.parent.ListaMaterias.append(diccionario)
            self.parent.ActualizarListaMaterias()
            self.close()