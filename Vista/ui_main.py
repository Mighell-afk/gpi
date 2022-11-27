# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main.ui'
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
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 100, 441, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_facultad = QPushButton(self.gridLayoutWidget)
        self.btn_facultad.setObjectName(u"btn_facultad")
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

        self.gridLayout.addWidget(self.btn_facultad, 0, 0, 1, 1)

        self.btn_materia = QPushButton(self.gridLayoutWidget)
        self.btn_materia.setObjectName(u"btn_materia")
        self.btn_materia.setMinimumSize(QSize(0, 0))
        self.btn_materia.setMaximumSize(QSize(3000, 3000))
        self.btn_materia.setFont(font)
        self.btn_materia.setFocusPolicy(Qt.StrongFocus)
        self.btn_materia.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_materia, 0, 1, 1, 1)

        self.btn_carrera = QPushButton(self.gridLayoutWidget)
        self.btn_carrera.setObjectName(u"btn_carrera")
        self.btn_carrera.setMinimumSize(QSize(0, 0))
        self.btn_carrera.setMaximumSize(QSize(3000, 3000))
        self.btn_carrera.setFont(font)
        self.btn_carrera.setFocusPolicy(Qt.StrongFocus)
        self.btn_carrera.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_carrera, 1, 0, 1, 1)

        self.btn_malla = QPushButton(self.gridLayoutWidget)
        self.btn_malla.setObjectName(u"btn_malla")
        self.btn_malla.setMinimumSize(QSize(0, 0))
        self.btn_malla.setMaximumSize(QSize(3000, 3000))
        self.btn_malla.setFont(font)
        self.btn_malla.setFocusPolicy(Qt.StrongFocus)
        self.btn_malla.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_malla, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Gate", None))
        self.label.setText(QCoreApplication.translate("Form", u"Seleccione algun componente de la malla curricular", None))
        self.btn_facultad.setText(QCoreApplication.translate("Form", u"Facultad", None))
        self.btn_materia.setText(QCoreApplication.translate("Form", u"Materia", None))
        self.btn_carrera.setText(QCoreApplication.translate("Form", u"Carrera", None))
        self.btn_malla.setText(QCoreApplication.translate("Form", u"Malla curricular", None))
    # retranslateUi

