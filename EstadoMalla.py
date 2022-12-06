from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from Vista.UI_EstadoMalla import Ui_EstadoMalla
from conexion import BaseDeDatos
from eventos import *

class EstadoMalla(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.estadomalla = Ui_EstadoMalla()
        self.estadomalla.setupUi(self)
        self.parent = parent

        self.idMalla = -1

        self.estadomalla.btn_buscar.clicked.connect(lambda: self.ObtenerDatos())
        self.estadomalla.btn_altabaja.clicked.connect(lambda: self.CambiarEstado())

    def ObtenerDatos(self):
        codMalla = int(self.estadomalla.txt_codmalla.text())

        sql = "select fa.nombre, ca.nombre, ma.promocion, mo.descripcion, ma.activo from malla_curricular ma "
        sql += "inner join carrera ca on ma.idcarrera = ca.idcarrera "
        sql += "inner join facultad fa on ma.idfacultad = fa.idfacultad "
        sql += f"inner join modalidad mo on ma.idmodalidad = mo.idmodalidad where ma.idmalla_curricular = {codMalla}"

        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)

        datosMalla = self.cur.fetchall()

        if(datosMalla != []):

            if(datosMalla [0][4] == 1):
                self.estado = 0
            elif(datosMalla [0][4] == 0):
                self.estado = 1

            self.estadomalla.lbl_facultad.setText(datosMalla[0][0])
            self.estadomalla.lbl_carrera.setText(datosMalla[0][1])
            self.estadomalla.lbl_promocion.setText(str(datosMalla[0][2]))
            self.estadomalla.lbl_modalidad.setText(datosMalla[0][3])
            self.estadomalla.btn_altabaja.setEnabled(True)
            self.idMalla = codMalla
        else:
            InfoMsg(self,'Informacion','No existe dicha malla')

    def CambiarEstado(self):
        idMalla = int(self.estadomalla.txt_codmalla.text())
        sql = f"update malla_curricular SET activo = {self.estado} WHERE idmalla_curricular = {idMalla}"
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        self.con.commit()
        self.estadomalla.btn_altabaja.setEnabled(False)
        self.estadomalla.txt_codmalla.clear()
        self.parent.ActualizarMallas(self.parent.QueryForActive)

        if self.estado:
            ActualState = "Activo"
        else:
            ActualState = "Inactivo"
        InfoMsg(self,'Informacion',f'La malla se cambio a estado {ActualState} con exito')
        self.close()
        
