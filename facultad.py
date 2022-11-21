from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from AnadirFacultad import Addfacu
from Vista.ui_facultad import Ui_Facultad


class facultad(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(facultad, self).__init__()
        self.facultad = Ui_Facultad()
        self.facultad.setupUi(self)


        self.QueryForAll      = "select idfacultad,nombre,siglas from facultad"
        self.QueryForActive   = "select idfacultad,nombre,siglas from facultad where activo = 1"
        self.QueryForInactive = "select idfacultad,nombre,siglas from facultad where activo = 0"


        self.ActualizarFacultad(self.QueryForActive)
               
        # --- Botones 
        self.facultad.btn_agregar.clicked.connect(lambda:self.AbrirCargaFacu())
        self.facultad.btn_filtrar.clicked.connect(lambda:self.FilterPerQuery())
        # --- Buscar Facultad
        self.facultad.cbo_filterFacultad.setCurrentIndex(-1)
        self.facultad.cbo_filterFacultad.currentIndexChanged.connect(self.FilterTable)


    def FilterPerQuery(self):
         # --- RadioButton
        if self.facultad.rdb_all.isChecked() == True:
            print("All True")
            self.ActualizarFacultad(self.QueryForAll)

        elif self.facultad.rdb_activo.isChecked() == True:
            print("activo True")
            self.ActualizarFacultad(self.QueryForActive)
            
        elif self.facultad.rdb_inactivo.isChecked() == True:
            print("inactivo True")
            self.ActualizarFacultad(self.QueryForInactive)

    
    
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
    

    def AbrirCargaFacu(self):
        self.Addfacu = Addfacu(self)
        self.Addfacu.show()
        
        
    def FilterTable(self):
        filter_proxy_model = QSortFilterProxyModel()        
        filter_proxy_model.setSourceModel(modelTableCLientes)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        Filter = self.facultad.cbo_filterFacultad.currentIndex()
        filter_proxy_model.setFilterKeyColumn(Filter)
        self.facultad.txtBuscarFacultad.textChanged.connect(filter_proxy_model.setFilterFixedString)
        self.facultad.tablefacultad.setModel(filter_proxy_model) 




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = facultad()
    mi_aplicacion.show()
    sys.exit(app.exec_())


