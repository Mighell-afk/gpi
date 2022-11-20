from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys

#ESTE ES COMENTARIO DE DIEGO
#Este es de Dario

from Vista.ui_facultad import Ui_Facultad


class facultad(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(facultad, self).__init__()
        self.facultad = Ui_Facultad()
        self.facultad.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = facultad()
    mi_aplicacion.show()
    sys.exit(app.exec_())