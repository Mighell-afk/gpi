from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys


from Vista.ui_anadirFacultad import Ui_AnadirFacultad


class Addfacu(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(Addfacu, self).__init__()
        self.Addfacu = Ui_AnadirFacultad()
        self.Addfacu.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = Addfacu()
    mi_aplicacion.show()
    sys.exit(app.exec_())