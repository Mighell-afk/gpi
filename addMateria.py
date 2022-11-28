from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
#from ..conexion import BaseDeDatos
from Vista.ui_agregar_materia import Ui_CargarMateria


class AddMate(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(AddMate, self).__init__()
        self.addmateria = Ui_CargarMateria()
        self.addmateria.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = AddMate()
    mi_aplicacion.show()
    sys.exit(app.exec_())
