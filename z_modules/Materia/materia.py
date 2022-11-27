from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
#from ..conexion import BaseDeDatos
from Vista.Materia.ui_materia import Ui_Materia


class Materia(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(Materia, self).__init__()
        self.materia = Ui_Materia()
        self.materia.setupUi(self)








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = Materia()
    mi_aplicacion.show()
    sys.exit(app.exec_())

