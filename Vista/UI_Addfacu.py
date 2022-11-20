# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarFacultad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#import resources_rc

class Ui_AnadirFacultad(object):
    def setupUi(self, CargarProducto):
        if not CargarProducto.objectName():
            CargarProducto.setObjectName(u"CargarProducto")
        CargarProducto.setWindowModality(Qt.ApplicationModal)
        CargarProducto.resize(500, 270)
        CargarProducto.setMinimumSize(QSize(500, 270))
        CargarProducto.setMaximumSize(QSize(500, 1500))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        CargarProducto.setWindowIcon(icon)
        CargarProducto.setStyleSheet(u"QWidget{\n"
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
        self.label = QLabel(CargarProducto)
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
        self.gridLayoutWidget = QWidget(CargarProducto)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 80, 441, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.txt_nombreFacultad = QLineEdit(self.gridLayoutWidget)
        self.txt_nombreFacultad.setObjectName(u"txt_nombreFacultad")
        self.txt_nombreFacultad.setEnabled(True)
        self.txt_nombreFacultad.setMinimumSize(QSize(0, 0))
        self.txt_nombreFacultad.setMaximumSize(QSize(295, 16777215))
        self.txt_nombreFacultad.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_nombreFacultad, 0, 1, 1, 1)

        self.txt_siglas = QLineEdit(self.gridLayoutWidget)
        self.txt_siglas.setObjectName(u"txt_siglas")
        self.txt_siglas.setEnabled(True)
        self.txt_siglas.setMinimumSize(QSize(0, 0))
        self.txt_siglas.setMaximumSize(QSize(295, 16777215))

        self.gridLayout.addWidget(self.txt_siglas, 1, 1, 1, 1)

        self.btn_AnadirFacultad = QPushButton(CargarProducto)
        self.btn_AnadirFacultad.setObjectName(u"btn_AnadirFacultad")
        self.btn_AnadirFacultad.setGeometry(QRect(190, 210, 141, 41))
        self.btn_AnadirFacultad.setMinimumSize(QSize(116, 32))
        QWidget.setTabOrder(self.txt_nombreFacultad, self.btn_AnadirFacultad)

        self.retranslateUi(CargarProducto)

        QMetaObject.connectSlotsByName(CargarProducto)
    # setupUi

    def retranslateUi(self, CargarProducto):
        CargarProducto.setWindowTitle(QCoreApplication.translate("CargarProducto", u"Cargar Producto", None))
        self.label.setText(QCoreApplication.translate("CargarProducto", u"Agregar Facultad", None))
        self.label_8.setText(QCoreApplication.translate("CargarProducto", u"Siglas", None))
        self.label_10.setText(QCoreApplication.translate("CargarProducto", u"Nombre Facultad", None))
        self.btn_AnadirFacultad.setText(QCoreApplication.translate("CargarProducto", u"A\u00f1adir", None))
    # retranslateUi

