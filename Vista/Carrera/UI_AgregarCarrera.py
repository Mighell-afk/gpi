# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarCarrera.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Vista import resources

class Ui_AgregarCarrera(object):
    def setupUi(self, CargarFacultad):
        if not CargarFacultad.objectName():
            CargarFacultad.setObjectName(u"CargarFacultad")
        CargarFacultad.setWindowModality(Qt.ApplicationModal)
        CargarFacultad.resize(500, 312)
        CargarFacultad.setMinimumSize(QSize(500, 270))
        CargarFacultad.setMaximumSize(QSize(3000, 3000))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        CargarFacultad.setWindowIcon(icon)
        CargarFacultad.setStyleSheet(u"QWidget{\n"
"	color: #333;\n"
"	font: 9pt \"Segoe UI\";\n"
"}\n"
"/* ----------------- LineEdit  ----------------- */\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	border: 2px solid #1F54A3;\n"
"	padding-left: 10px;\n"
"	selection-color: white;\n"
"	selection-background-color: #2A3C57;\n"
"    color: black;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(98, 114, 164);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #2A3C57;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ----------------- Button ----------------- */\n"
"QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
" QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
" QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}\n"
"\n"
"/* ----------------- CheckBox ----------------- */\n"
"\n"
"QCheckBox::indicator {\n"
"	border : 1px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 15px;"
                        "\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: #286FD6;\n"
"	border : 1px solid #286FD6;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border : 1px solid #1F54A3;\n"
"    background: 3px solid #1F54A3;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"\n"
"/* ----------------- QDateEdit ----------------- */\n"
"QDateTimeEdit{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #1F54A3;\n"
"    color: black;\n"
"}\n"
"QDateTimeEdit:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"\n"
"QDateTimeEdit:focus {\n"
"	border: 2px solid #2A3C57;\n"
"}\n"
"\n"
"\n"
"QDateTimeEdit::up-button {\n"
"    border-image: url(:/icons/images/icons/cil-arrow-top.png); \n"
"}\n"
"\n"
"QDateTimeEdit::down-button {\n"
"    border-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
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
"")
        self.label = QLabel(CargarFacultad)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 0, 221, 71))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 25 16pt \"Microsoft YaHei UI Light\";")
        self.gridLayoutWidget = QWidget(CargarFacultad)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 80, 441, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.txt_nombreCarrera = QLineEdit(self.gridLayoutWidget)
        self.txt_nombreCarrera.setObjectName(u"txt_nombreCarrera")
        self.txt_nombreCarrera.setEnabled(True)
        self.txt_nombreCarrera.setMinimumSize(QSize(0, 0))
        self.txt_nombreCarrera.setMaximumSize(QSize(295, 16777215))
        self.txt_nombreCarrera.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_nombreCarrera, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.txt_codCarrera = QLineEdit(self.gridLayoutWidget)
        self.txt_codCarrera.setObjectName(u"txt_codCarrera")
        self.txt_codCarrera.setEnabled(True)
        self.txt_codCarrera.setMinimumSize(QSize(0, 0))
        self.txt_codCarrera.setMaximumSize(QSize(295, 16777215))
        self.txt_codCarrera.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_codCarrera, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.cboFacultad = QComboBox(self.gridLayoutWidget)
        self.cboFacultad.setObjectName(u"cboFacultad")

        self.gridLayout.addWidget(self.cboFacultad, 2, 1, 1, 1)

        self.btn_AnadirCarrera = QPushButton(CargarFacultad)
        self.btn_AnadirCarrera.setObjectName(u"btn_AnadirCarrera")
        self.btn_AnadirCarrera.setGeometry(QRect(170, 220, 141, 41))
        self.btn_AnadirCarrera.setMinimumSize(QSize(116, 32))
        QWidget.setTabOrder(self.txt_nombreCarrera, self.btn_AnadirCarrera)

        self.retranslateUi(CargarFacultad)

        QMetaObject.connectSlotsByName(CargarFacultad)
    # setupUi

    def retranslateUi(self, CargarFacultad):
        CargarFacultad.setWindowTitle(QCoreApplication.translate("CargarFacultad", u"Cargar Producto", None))
        self.label.setText(QCoreApplication.translate("CargarFacultad", u"Agregar Carrera", None))
        self.label_10.setText(QCoreApplication.translate("CargarFacultad", u"Nombre Carrera", None))
        self.label_8.setText(QCoreApplication.translate("CargarFacultad", u"Facultad", None))
        self.label_11.setText(QCoreApplication.translate("CargarFacultad", u"Codigo Carrera", None))
        self.btn_AnadirCarrera.setText(QCoreApplication.translate("CargarFacultad", u"A\u00f1adir", None))
    # retranslateUi

