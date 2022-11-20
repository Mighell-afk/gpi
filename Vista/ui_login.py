# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#import resources

class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.setAttribute(Qt.WA_TranslucentBackground)                 
            MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.resize(640, 500)
        MainWindow.setMinimumSize(QSize(640, 500))
        MainWindow.setMaximumSize(QSize(640, 500))
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"/*\n"
"	normal: #1F54A3\n"
"\n"
"	hover: #286FD6\n"
"\n"
"pressed :	#2A3C57\n"
"}\n"
"*/\n"
"\n"
"\n"
"\n"
"/* --------------- LineEdits --------------- */\n"
"\n"
"QLineEdit {\n"
"background-color: transparent;\n"
"border: none;\n"
"font: 63 13pt \"Raleway SemiBold\";\n"
"color: #efefef\n"
"}\n"
"\n"
"\n"
"/* --------------- FRAMES --------------- */\n"
"\n"
"/*  Frame izquierda  */\n"
"#frameLeft.QFrame {\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	background-color:#D01A19;\n"
"	font: 63 13pt \"Raleway SemiBold\";\n"
"	color: red;\n"
"}\n"
" \n"
"/*  Frame derecha  */\n"
"#frameRight.QFrame {\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	/*background-color: #1F54A3;*/\n"
"	background-color:qlineargradient(spread:pad, x1:0.607022, y1:0.86, x2:1, y2:1, stop:0.2966 rgba(31, 84, 163, 255), stop:1 rgba(65, 63, 154, 255));\n"
"	font: 63 13pt \"Raleway SemiBold\";\n"
"	color: red;\n"
"}\n"
"\n"
"#frameLog.QFrame {\n"
"background-color:  #f8f8f2;\n"
"\n"
"\n"
"}\n"
"/* --------------- ICONOS --------------"
                        "- */\n"
"\n"
"/*  Frame icono  */\n"
"#lbl_iconLogo.QLabel {\n"
"	background-color:transparent;\n"
"	image: url(:/images/images/images/Logo_vertical.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frameLeft = QFrame(self.StyleSheet)
        self.frameLeft.setObjectName(u"frameLeft")
        self.frameLeft.setGeometry(QRect(100, 20, 330, 441))
        self.frameLeft.setStyleSheet(u"")
        self.frameLeft.setFrameShape(QFrame.StyledPanel)
        self.frameLeft.setFrameShadow(QFrame.Raised)
        self.lbl_titulo = QLabel(self.frameLeft)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(0, 30, 281, 61))
        self.lbl_titulo.setStyleSheet(u"/* --------------- LABELS --------------- */\n"
"\n"
"QLabel{\n"
"	color: #f8f8f2;\n"
"	font: 20pt \"Microsoft YaHei UI Light\";\n"
"}\n"
"")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_iconLogo = QLabel(self.frameLeft)
        self.lbl_iconLogo.setObjectName(u"lbl_iconLogo")
        self.lbl_iconLogo.setGeometry(QRect(20, 120, 181, 221))
        self.lbl_iconLogo.setStyleSheet(u"QLabel {\n"
"	background-color:transparent;\n"
"	image: url(:/images/images/images/descarga.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	\n"
"}\n"
"")
        self.frameRight = QFrame(self.StyleSheet)
        self.frameRight.setObjectName(u"frameRight")
        self.frameRight.setGeometry(QRect(300, 10, 338, 471))
        self.frameRight.setStyleSheet(u"")
        self.frameRight.setFrameShape(QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QFrame.Raised)
        self.txtUser = QLineEdit(self.frameRight)
        self.txtUser.setObjectName(u"txtUser")
        self.txtUser.setGeometry(QRect(60, 200, 201, 31))
        self.txtUser.setStyleSheet(u"")
        self.txtPass = QLineEdit(self.frameRight)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(60, 280, 221, 31))
        self.txtPass.setStyleSheet(u"")
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.btn_logEnabPass = QPushButton(self.frameRight)
        self.btn_logEnabPass.setObjectName(u"btn_logEnabPass")
        self.btn_logEnabPass.setGeometry(QRect(280, 280, 28, 28))
        self.btn_logEnabPass.setMinimumSize(QSize(28, 28))
        self.btn_logEnabPass.setMaximumSize(QSize(28, 28))
        self.btn_logEnabPass.setStyleSheet(u"/* --------------- BOTONES --------------- */\n"
"\n"
" QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
" QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/eye_open_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logEnabPass.setIcon(icon)
        self.btn_logEnabPass.setIconSize(QSize(20, 20))
        self.btn_login = QPushButton(self.frameRight)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(50, 360, 221, 51))
        self.btn_login.setStyleSheet(u"/* --------------- LABELS --------------- */\n"
"\n"
"\n"
"\n"
"/* --------------- BOTONES --------------- */\n"
"\n"
" QPushButton {\n"
"	color: #f8f8f2;\n"
"	font: 15pt \"Microsoft YaHei UI Light\";\n"
"	border: 2px solid #286FD6;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
" QPushButton:pressed {	\n"
"	border: 2px solid #286FD6;\n"
"\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}\n"
"\n"
"")
        self.lbl_logEstado = QLabel(self.frameRight)
        self.lbl_logEstado.setObjectName(u"lbl_logEstado")
        self.lbl_logEstado.setGeometry(QRect(50, 430, 221, 31))
        self.lbl_logEstado.setStyleSheet(u"font: 25 10pt \"Microsoft YaHei UI Light\";")
        self.lbl_logEstado.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.btn_logCerrar = QPushButton(self.frameRight)
        self.btn_logCerrar.setObjectName(u"btn_logCerrar")
        self.btn_logCerrar.setGeometry(QRect(290, 10, 28, 28))
        self.btn_logCerrar.setMinimumSize(QSize(28, 28))
        self.btn_logCerrar.setMaximumSize(QSize(28, 28))
        self.btn_logCerrar.setStyleSheet(u"/* --------------- BOTONES --------------- */\n"
"\n"
" QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
" QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logCerrar.setIcon(icon1)
        self.btn_logCerrar.setIconSize(QSize(27, 27))
        self.line = QFrame(self.frameRight)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(60, 290, 221, 41))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.frameRight)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(60, 215, 201, 31))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.lbl_user = QLabel(self.frameRight)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setGeometry(QRect(20, 200, 31, 31))
        self.lbl_user.setStyleSheet(u"QLabel {\n"
"	background-color:transparent;\n"
"	image: url(:/icons/images/icons/cil-user.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"")
        self.label = QLabel(self.frameRight)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 280, 31, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"	background-color:transparent;\n"
"	image: url(:/icons/images/icons/cil-lock-locked.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	\n"
"}\n"
"")
        self.lbl_user_2 = QLabel(self.frameRight)
        self.lbl_user_2.setObjectName(u"lbl_user_2")
        self.lbl_user_2.setGeometry(QRect(110, 50, 101, 111))
        self.lbl_user_2.setStyleSheet(u"QLabel {\n"
"	background-color:transparent;\n"
"	image: url(:/images/images/images/user.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.StyleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lbl_iconLogo.setText("")
        self.txtUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu usuario", None))
        self.txtPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu contrase\u00f1a", None))
        self.btn_logEnabPass.setText("")
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.lbl_logEstado.setText("")
        self.btn_logCerrar.setText("")
        self.lbl_user.setText("")
        self.label.setText("")
        self.lbl_user_2.setText("")
    # retranslateUi

