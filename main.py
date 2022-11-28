from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from materia import Materia
from facultad import facultad
from Vista.ui_main import Ui_Main


class program(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(program, self).__init__()
        self.program = Ui_Main()
        self.program.setupUi(self)


        self.program.btn_facultad.clicked.connect(lambda:self.OpenFacultad())
        self.program.btn_materia.clicked.connect(lambda:self.OpenMateria())
        self.program.btn_malla.setVisible(False)


    def OpenFacultad(self):
        self.facu = facultad()
        self.facu.show()
        self.close()
    
    def OpenMateria(self):
        self.materia = Materia()
        self.materia.show()  

    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = program()
    mi_aplicacion.show()
    sys.exit(app.exec_())