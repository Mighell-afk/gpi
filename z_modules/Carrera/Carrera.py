from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from ..conexion import BaseDeDatos
from z_modules.Carrera.AnadirCarrera import AddCarrera
from Vista.Carrera.UI_Carrera import Ui_MenuCarrera
from z_modules.Carrera.EliminarCarrera import eliminarCarrera
from z_modules.Carrera.ModificarCarrera import modificar


class carrera(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(carrera, self).__init__()
        self.carrera = Ui_MenuCarrera()
        self.carrera.setupUi(self)
        


        self.QueryForAll      = "select mt.idcarrera, mt.nombre, fa.nombre as facultad from carrera mt inner join facultad fa on mt.idfacultad = fa.idfacultad"
        self.QueryForActive   = "select mt.idcarrera, mt.nombre, fa.nombre as facultad from carrera mt inner join facultad fa on mt.idfacultad = fa.idfacultad where mt.activo = 1"
        self.QueryForInactive = "select mt.idcarrera, mt.nombre, fa.nombre as facultad from carrera mt inner join facultad fa on mt.idfacultad = fa.idfacultad where mt.activo = 0"


        self.ActualizarCarrera(self.QueryForActive)
               
        # --- Botones 
        self.carrera.btn_agregar.clicked.connect(lambda:self.AbrirCargaCarrera())

        self.carrera.btn_modificar.clicked.connect(lambda:self.AbrirModificarCarrera())

        self.carrera.btn_eliminar.clicked.connect(lambda:self.AbrirEliminarCarrera())
        self.carrera.btn_filtrar.clicked.connect(lambda:self.FilterPerQuery())

        # --- Buscar Facultad
        self.carrera.cbo_filterCarrera.setCurrentIndex(-1)
        self.carrera.cbo_filterCarrera.currentIndexChanged.connect(self.FilterTable)
   
    
    def AbrirCargaCarrera(self):
        self.AddCarrera = AddCarrera(self)
        self.AddCarrera.show()
        
  
    def AbrirEliminarCarrera(self):
        self.facu = eliminarCarrera(self)
        self.facu.show()
         
    def AbrirModificarCarrera(self):
        self.facu = modificar(self)
        self.facu.show()


    def FilterPerQuery(self):
         # --- RadioButton
        if self.carrera.rdb_all.isChecked() == True:
            self.ActualizarCarrera(self.QueryForAll)

        elif self.carrera.rdb_activo.isChecked() == True:
            self.ActualizarCarrera(self.QueryForActive)
            
        elif self.carrera.rdb_inactivo.isChecked() == True:
            self.ActualizarCarrera(self.QueryForInactive)
    

    def ActualizarCarrera(self,query):
        self.carrera.cbo_filterCarrera.setCurrentIndex(-1)
        global modelTableCLientes
        headerCliente = ["Codigo","Nombre Carrera","Facultad"]
        # ---------- Obtener datos de la tabla clientes ----------
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(query)
        DatosCLiente = self.cur.fetchall()
        filas = len(DatosCLiente)
        columnas = len(headerCliente)
        modelTableCLientes = QStandardItemModel(filas, columnas)
        modelTableCLientes.setHorizontalHeaderLabels(headerCliente)
        # ---------- Cargar cliente a la tabla ----------
        for fila in range(filas):
            for columna in range(columnas):
                modelTableCLientes.setItem(fila, columna, QStandardItem(str(DatosCLiente[fila][columna])))
        self.carrera.tablecarrera.setModel(modelTableCLientes)
        # ---------- Establecer anchos a las columnas (personalizados) ----------
        for indice, ancho in enumerate((180,800,180),start= 0):
            self.carrera.tablecarrera.setColumnWidth(indice,ancho)
    
    
    def FilterTable(self):
        filter_proxy_model = QSortFilterProxyModel()        
        filter_proxy_model.setSourceModel(modelTableCLientes)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        Filter = self.carrera.cbo_filterCarrera.currentIndex()
        filter_proxy_model.setFilterKeyColumn(Filter)
        self.carrera.txtBuscarCarrera.textChanged.connect(filter_proxy_model.setFilterFixedString)
        self.carrera.tablecarrera.setModel(filter_proxy_model) 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = carrera()
    mi_aplicacion.show()
    sys.exit(app.exec_())

