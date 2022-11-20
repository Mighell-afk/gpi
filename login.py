from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys

from Vista.ui_login import Ui_Login
from main import program

class login(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(login, self).__init__()
        self.login = Ui_Login()
        self.login.setupUi(self)
        self.Animation()
        self.main = program()
        
        #---- CREDENCIALES DEL USUARIO
        self.USUARIO = "Admin" 
        self.PASSWORD = "12345"

        #---- Boton Cerrar
        self.login.btn_logCerrar.clicked.connect(lambda:self.close())
        #---- Boton Login
        self.login.btn_login.clicked.connect(lambda:self.ingresar())


    def ingresar(self):
        User = self.login.txtUser.text()
        Passw = self.login.txtPass.text()
        print(User,Passw)
        if User == self.USUARIO and Passw == self.PASSWORD:
            print("logueado correctamente")
            self.main.show()
        else:
            self.login.lbl_logEstado.setText("credenciales incorrectos")



    def Animation(self):
        self.animation = QPropertyAnimation(self.login.frameLeft, b"geometry")
        self.animation.setDuration(1200)
        self.animation.setStartValue(QRect(309,30, 330, 441))
        self.animation.setEndValue(QRect(25, 30, 330, 441))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = login()
    mi_aplicacion.show()
    sys.exit(app.exec_())