# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarMateria.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Vista import resources


class Ui_CargarMateria(object):
    def setupUi(self, CargarMateria):
        if not CargarMateria.objectName():
            CargarMateria.setObjectName(u"CargarMateria")
        CargarMateria.setWindowModality(Qt.ApplicationModal)
        CargarMateria.resize(500, 312)
        CargarMateria.setMinimumSize(QSize(500, 270))
        CargarMateria.setMaximumSize(QSize(3000, 3000))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        CargarMateria.setWindowIcon(icon)
        CargarMateria.setStyleSheet(u"QWidget{\n"
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
        self.label = QLabel(CargarMateria)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 221, 71))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 25 16pt \"Microsoft YaHei UI Light\";")
        self.gridLayoutWidget = QWidget(CargarMateria)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 80, 441, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.txt_siglas = QLineEdit(self.gridLayoutWidget)
        self.txt_siglas.setObjectName(u"txt_siglas")
        self.txt_siglas.setEnabled(True)
        self.txt_siglas.setMinimumSize(QSize(0, 0))
        self.txt_siglas.setMaximumSize(QSize(295, 16777215))

        self.gridLayout.addWidget(self.txt_siglas, 2, 1, 1, 1)

        self.txt_codfacultad = QLineEdit(self.gridLayoutWidget)
        self.txt_codfacultad.setObjectName(u"txt_codfacultad")
        self.txt_codfacultad.setEnabled(True)
        self.txt_codfacultad.setMinimumSize(QSize(0, 0))
        self.txt_codfacultad.setMaximumSize(QSize(295, 16777215))
        self.txt_codfacultad.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_codfacultad, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.cbo_facultad = QComboBox(self.gridLayoutWidget)
        self.cbo_facultad.setObjectName(u"cbo_facultad")
        self.cbo_facultad.setStyleSheet(u"/* ----------------- QComboBox ----------------- */\n"
"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #1F54A3;\n"
"    color: black;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: white;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	background-image:url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: white;	\n"
"	background-color: #1F54A3;\n"
"	\n"
"	selection-background-color: #1F54A3;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.cbo_facultad, 1, 1, 1, 1)

        self.btn_AnadirFacultad = QPushButton(CargarMateria)
        self.btn_AnadirFacultad.setObjectName(u"btn_AnadirFacultad")
        self.btn_AnadirFacultad.setGeometry(QRect(170, 220, 141, 41))
        self.btn_AnadirFacultad.setMinimumSize(QSize(116, 32))

        self.retranslateUi(CargarMateria)

        QMetaObject.connectSlotsByName(CargarMateria)
    # setupUi

    def retranslateUi(self, CargarMateria):
        CargarMateria.setWindowTitle(QCoreApplication.translate("CargarMateria", u"Cargar Materia", None))
        self.label.setText(QCoreApplication.translate("CargarMateria", u"Agregar Materia", None))
        self.label_10.setText(QCoreApplication.translate("CargarMateria", u"Nombre Facultad", None))
        self.label_8.setText(QCoreApplication.translate("CargarMateria", u"Nombre de materia", None))
        self.label_11.setText(QCoreApplication.translate("CargarMateria", u"Codigo Materia", None))
        self.btn_AnadirFacultad.setText(QCoreApplication.translate("CargarMateria", u"A\u00f1adir", None))
    # retranslateUi

