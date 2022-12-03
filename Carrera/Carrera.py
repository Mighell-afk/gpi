from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from ..conexion import BaseDeDatos
from z_modules.Carrera.AnadirCarrera import AddCarrera
from Vista.Carrera.UI_Carrera import Ui_MenuCarrera
from z_modules.Carrera.EliminarCarrera import eliminarCarrera


class carrera(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(carrera, self).__init__()
        self.carrera = Ui_MenuCarrera()
        self.carrera.setupUi(self)
        


        self.QueryForAll      = "select idfacultad,nombre,siglas from facultad"
        self.QueryForActive   = "select idfacultad,nombre,siglas from facultad where activo = 1"
        self.QueryForInactive = "select idfacultad,nombre,siglas from facultad where activo = 0"


        #self.ActualizarFacultad(self.QueryForActive)
               
        # --- Botones 
        self.carrera.btn_agregar.clicked.connect(lambda:self.AbrirCargaCarrera())
        self.carrera.btn_eliminar.clicked.connect(lambda:self.AbrirEliminarCarrera())

        # --- Buscar Facultad
        #self.carrera.cbo_filterCarrera.setCurrentIndex(-1)
        #self.carrera.cbo_filterCarrera.currentIndexChanged.connect(self.FilterTable)
   
    
    def AbrirCargaCarrera(self):
        self.AddCarrera = AddCarrera(self)
        self.AddCarrera.show()
        
  
    def AbrirEliminarCarrera(self):
        self.facu = eliminarCarrera(self)
        self.facu.show()
         

    '''
    def FilterPerQuery(self):
         # --- RadioButton
        if self.facultad.rdb_all.isChecked() == True:
            self.ActualizarFacultad(self.QueryForAll)

        elif self.facultad.rdb_activo.isChecked() == True:
            self.ActualizarFacultad(self.QueryForActive)
            
        elif self.facultad.rdb_inactivo.isChecked() == True:
            self.ActualizarFacultad(self.QueryForInactive)

    '''
    '''
    def ActualizarFacultad(self,query):
        self.facultad.cbo_filterFacultad.setCurrentIndex(-1)
        global modelTableCLientes
        headerCliente = ["Codigo","Nombre Facultad","Siglas"]
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
        self.facultad.tablefacultad.setModel(modelTableCLientes)
        # ---------- Establecer anchos a las columnas (personalizados) ----------
        for indice, ancho in enumerate((180,800,180),start= 0):
            self.facultad.tablefacultad.setColumnWidth(indice,ancho)
    
    '''
    
    ''' 
    def FilterTable(self):
        filter_proxy_model = QSortFilterProxyModel()        
        filter_proxy_model.setSourceModel(modelTableCLientes)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        Filter = self.facultad.cbo_filterFacultad.currentIndex()
        filter_proxy_model.setFilterKeyColumn(Filter)
        self.facultad.txtBuscarFacultad.textChanged.connect(filter_proxy_model.setFilterFixedString)
        self.facultad.tablefacultad.setModel(filter_proxy_model) 
    '''



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = carrera()
    mi_aplicacion.show()
    sys.exit(app.exec_())

