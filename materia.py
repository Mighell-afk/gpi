from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from Vista.ui_materia import Ui_Materia
from addMateria import AddMate
from ModificarMateria import ModificarMateria
from EliminarMateria import EliminarMateria
from EstadoMateria import estmate


class Materia(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(Materia, self).__init__()
        self.materia = Ui_Materia()
        self.materia.setupUi(self)

        self.QueryForAll      = "select idMateria,mt.Nombre as Materia,fa.nombre as facultad from materia mt INNER JOIN facultad fa on (mt.idfacultad = fa.idfacultad)"
        self.QueryForActive   = "select idMateria,mt.Nombre as Materia,fa.nombre as facultad from materia mt INNER JOIN facultad fa on (mt.idfacultad = fa.idfacultad) WHERE mt.Activo =1"
        self.QueryForInactive = "select idMateria,mt.Nombre as Materia,fa.nombre as facultad from materia mt INNER JOIN facultad fa on (mt.idfacultad = fa.idfacultad) WHERE mt.Activo =0"

        self.ActualizarMateria(self.QueryForActive)

         # --- Botones 
        self.materia.btn_agregar.clicked.connect(lambda:self.AbrirCargaMateria())
        self.materia.btn_modificar.clicked.connect(lambda:self.AbrirEditarFacu())
        self.materia.btn_eliminar.clicked.connect(lambda:self.AbrirEliminarFacu())
        self.materia.btn_baja.clicked.connect(lambda:self.AbrirEstadoFacu())
        self.materia.btn_filtrar.clicked.connect(lambda:self.FilterPerQuery())

        # # --- Buscar Facultad
        self.materia.cbo_filterMateria.setCurrentIndex(-1)
        self.materia.cbo_filterMateria.currentIndexChanged.connect(self.FilterTable)
   
    
    def AbrirCargaMateria(self):
        self.addmate = AddMate(self)
        self.addmate.show()
        
    def AbrirEditarFacu(self):
        self.edimate = ModificarMateria(self)
        self.edimate.show()

    def AbrirEliminarFacu(self):
        self.elimate = EliminarMateria(self)
        self.elimate.show()
    
    def AbrirEstadoFacu(self):
        self.estmate = estmate(self)
        self.estmate.show()

        


    def FilterPerQuery(self):
         # --- RadioButton
        if self.materia.rdb_all.isChecked() == True:
            self.ActualizarMateria(self.QueryForAll)

        elif self.materia.rdb_activo.isChecked() == True:
            self.ActualizarMateria(self.QueryForActive)
            
        elif self.materia.rdb_inactivo.isChecked() == True:
            self.ActualizarMateria(self.QueryForInactive)

    
    
    def ActualizarMateria(self,query):
        self.materia.cbo_filterMateria.setCurrentIndex(-1)
        global modelTableCLientes
        headerCliente = ["Codigo","Nombre Materia","Nombre Facultad"]
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
        self.materia.tablemateria.setModel(modelTableCLientes)
        # ---------- Establecer anchos a las columnas (personalizados) ----------
        for indice, ancho in enumerate((180,500,500),start= 0):
            self.materia.tablemateria.setColumnWidth(indice,ancho)
    

    
        
    def FilterTable(self):
        filter_proxy_model = QSortFilterProxyModel()        
        filter_proxy_model.setSourceModel(modelTableCLientes)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        Filter = self.materia.cbo_filterMateria.currentIndex()
        filter_proxy_model.setFilterKeyColumn(Filter)
        self.materia.txtBuscar.textChanged.connect(filter_proxy_model.setFilterFixedString)
        self.materia.tablemateria.setModel(filter_proxy_model) 

    def closeEvent(self, event: QCloseEvent):
        from main import program
        self.program = program()
        self.program.show()
    





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = Materia()
    mi_aplicacion.show()
    sys.exit(app.exec_())

