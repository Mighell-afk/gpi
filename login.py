from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys

#ESTE ES COMENTARIO DE DIEGO
#Este es de Dario

from Vista.ui_login import Ui_Login
from main import program

class login(QtWidgets.QMainWindow):
   
   
    def __init__(self):
        super(login, self).__init__()
        self.login = Ui_Login()
        self.login.setupUi(self)
        self.Animation()
        self.main = program()
        self.estado = True
        
        #---- CREDENCIALES DEL USUARIO
        self.USUARIO = "Admin" 
        self.PASSWORD = "12345"

        #---- Boton Cerrar
        self.login.btn_logCerrar.clicked.connect(lambda:self.close())
        #---- Boton Login
        self.login.btn_login.clicked.connect(lambda:self.ingresar())
        #---- Boton Mostrar contraseÃ±a
        self.login.btn_logEnabPass.clicked.connect(lambda:self.presionar())
        
    def presionar(self):
        if self.estado:
            self.login.btn_logEnabPass.setIcon(QIcon(u":/icons/images/icons/eye_open_icon.svg"))
            self.login.txtPass.setEchoMode(QLineEdit.EchoMode.Password)
            self.estado = False
        else:
            self.login.btn_logEnabPass.setIcon(QIcon(u":/icons/images/icons/eye_close_icon.svg"))
            self.login.txtPass.setEchoMode(QLineEdit.EchoMode.Normal)
            self.estado = True
             


    def ingresar(self):
        User = self.login.txtUser.text()
        Passw = self.login.txtPass.text()
        print(User,Passw)
        if User == self.USUARIO and Passw == self.PASSWORD:
            print("logueado correctamente")
            self.main.show()
        else:
            self.login.lbl_logEstado.setText("Nombre de usuario o contraseña incorrectos")



    def Animation(self):
        self.animation = QPropertyAnimation(self.login.frameLeft, b"geometry")
        self.animation.setDuration(1200)
        self.animation.setStartValue(QRect(309,30, 330, 441))
        self.animation.setEndValue(QRect(100, 30, 330, 441))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = login()
    mi_aplicacion.show()
    sys.exit(app.exec_())