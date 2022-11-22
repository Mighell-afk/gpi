# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Vista import resources

class Ui_Main(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(593, 575)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(680, 680))
        Form.setFocusPolicy(Qt.StrongFocus)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-browser.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color:#2c313a;\n"
"	color: rgb(221, 221, 221);\n"
"	font: 18px \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	font-size:25px;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: none;  \n"
"	color:#f8f8f2;\n"
"	border-radius: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"	background-color:#1F54A3;\n"
"	border: 2px solid#1F54A3 ;\n"
"	 border-style: solid;\n"
"	border-radius: 15px; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"	 border-style: solid;\n"
"	border-radius: 15px; \n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 471, 31))
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_facultad = QPushButton(Form)
        self.btn_facultad.setObjectName(u"btn_facultad")
        self.btn_facultad.setGeometry(QRect(200, 90, 221, 101))
        self.btn_facultad.setMinimumSize(QSize(0, 0))
        self.btn_facultad.setMaximumSize(QSize(3000, 3000))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_facultad.setFont(font)
        self.btn_facultad.setFocusPolicy(Qt.StrongFocus)
        self.btn_facultad.setStyleSheet(u"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Menu", None))
        self.label.setText(QCoreApplication.translate("Form", u"Seleccione algun componente de la malla curricular", None))
        self.btn_facultad.setText(QCoreApplication.translate("Form", u"Facultad", None))
    # retranslateUi

