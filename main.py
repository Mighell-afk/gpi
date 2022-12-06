from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from Carrera import carrera
from facultad import facultad
from materia import Materia
from malla_curricular import malla_curricular

from Vista.ui_main import Ui_Main

class program(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(program, self).__init__()
        self.program = Ui_Main()
        self.program.setupUi(self)

        self.program.btn_facultad.clicked.connect(lambda:self.OpenFacultad())
        self.program.btn_materia.clicked.connect(lambda:self.OpenMateria())
        self.program.btn_carrera.clicked.connect(lambda:self.OpenCarrera())
        self.program.btn_malla.clicked.connect(lambda:self.OpenMalla())


    def OpenFacultad(self):
        self.facu = facultad()
        self.facu.show()
        self.close()
    
    def OpenMateria(self):
        self.materia = Materia()
        self.materia.show()
        self.close()

    def OpenCarrera(self):
        self.carrera = carrera()
        self.carrera.show()
        self.close()
    
    def OpenMalla(self):
        self.malla = malla_curricular()
        self.malla.show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = program()
    mi_aplicacion.show()
    sys.exit(app.exec_())