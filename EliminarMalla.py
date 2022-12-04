from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from conexion import BaseDeDatos
import sys

from Vista.UI_EliminarMalla import Ui_EliminarMalla
from eventos import *

class EliminarMalla(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.eliminarMalla = Ui_EliminarMalla()
        self.eliminarMalla.setupUi(self)
        self.parent = parent

        self.idMalla = -1

        self.eliminarMalla.btn_buscar.clicked.connect(lambda: self.ObtenerDatos())
        self.eliminarMalla.btn_eliminar.clicked.connect(lambda: self.EliminarMalla())

    def ObtenerDatos(self):
        codMalla = int(self.eliminarMalla.txt_codcarrera.text())

        sql = "select fa.nombre, ca.nombre, ma.promocion, mo.descripcion from malla_curricular ma "
        sql += "inner join carrera ca on ma.idcarrera = ca.idcarrera "
        sql += "inner join facultad fa on ma.idfacultad = fa.idfacultad "
        sql += f"inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.idmalla_curricular = {codMalla}"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)

        datosMalla = self.cur.fetchall()

        if(datosMalla != []):
            self.eliminarMalla.lbl_facultad.setText(datosMalla[0][0])
            self.eliminarMalla.lbl_carrera.setText(datosMalla[0][1])
            self.eliminarMalla.lbl_promocion.setText(str(datosMalla[0][2]))
            self.eliminarMalla.lbl_modalidad.setText(datosMalla[0][3])
            self.eliminarMalla.btn_eliminar.setEnabled(True)
            self.idMalla = codMalla
        else:
            InfoMsg(self,'Informacion','No existe dicha malla')

    def EliminarMalla(self):
        if (self.idMalla != -1):
            self.connect = BaseDeDatos()
            self.con = self.connect.con
            # try:
            sql = f"delete from detalle_prerrequisito where detalle_idmalla = {self.idMalla}"
            
            self.cur = self.con.cursor()
            self.cur.execute(sql)

            sql = f"delete from detalle_malla where idmalla_curricular = {self.idMalla}"
            self.cur = self.con.cursor()
            self.cur.execute(sql)

            sql = f"delete from malla_curricular where idmalla_curricular = {self.idMalla}"
            self.cur = self.con.cursor()
            self.cur.execute(sql)
            
            self.con.commit()

            self.parent.ActualizarMallas(self.parent.QueryForAll)

            InfoMsg(self,'Informacion','Malla eliminada correctamente')

            # except:
            #     print("jajaj")
            #     self.con.rollback()
