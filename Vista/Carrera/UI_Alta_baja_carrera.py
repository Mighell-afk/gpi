# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alta_baja_carrera.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AltaBajaCarrera(object):
    def setupUi(self, AltaBajaCarrera):
        if not AltaBajaCarrera.objectName():
            AltaBajaCarrera.setObjectName(u"AltaBajaCarrera")
        AltaBajaCarrera.setWindowModality(Qt.ApplicationModal)
        AltaBajaCarrera.resize(572, 270)
        AltaBajaCarrera.setMinimumSize(QSize(500, 270))
        AltaBajaCarrera.setMaximumSize(QSize(3000, 3000))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        AltaBajaCarrera.setWindowIcon(icon)
        AltaBajaCarrera.setStyleSheet(u"QWidget{\n"
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
        self.label = QLabel(AltaBajaCarrera)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 0, 341, 71))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 25 16pt \"Microsoft YaHei UI Light\";")
        self.gridLayoutWidget = QWidget(AltaBajaCarrera)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 80, 441, 71))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_buscar = QPushButton(self.gridLayoutWidget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setMinimumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-paper-plane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_buscar, 0, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.txt_codcarrera = QLineEdit(self.gridLayoutWidget)
        self.txt_codcarrera.setObjectName(u"txt_codcarrera")
        self.txt_codcarrera.setEnabled(True)
        self.txt_codcarrera.setMinimumSize(QSize(0, 0))
        self.txt_codcarrera.setMaximumSize(QSize(295, 16777215))
        self.txt_codcarrera.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_codcarrera, 0, 1, 1, 1)

        self.lbl_nombrecarrera = QLabel(self.gridLayoutWidget)
        self.lbl_nombrecarrera.setObjectName(u"lbl_nombrecarrera")

        self.gridLayout.addWidget(self.lbl_nombrecarrera, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.btn_cambiarEstado = QPushButton(AltaBajaCarrera)
        self.btn_cambiarEstado.setObjectName(u"btn_cambiarEstado")
        self.btn_cambiarEstado.setEnabled(False)
        self.btn_cambiarEstado.setGeometry(QRect(220, 180, 141, 41))
        self.btn_cambiarEstado.setMinimumSize(QSize(116, 32))

        self.retranslateUi(AltaBajaCarrera)

        QMetaObject.connectSlotsByName(AltaBajaCarrera)
    # setupUi

    def retranslateUi(self, AltaBajaCarrera):
        AltaBajaCarrera.setWindowTitle(QCoreApplication.translate("AltaBajaCarrera", u"Alta/Baja Carrera", None))
        self.label.setText(QCoreApplication.translate("AltaBajaCarrera", u"Activar/Desactivar Carrera", None))
        self.btn_buscar.setText("")
        self.label_11.setText(QCoreApplication.translate("AltaBajaCarrera", u"Codigo Carrera", None))
        self.lbl_nombrecarrera.setText("")
        self.label_12.setText(QCoreApplication.translate("AltaBajaCarrera", u"Descripcion", None))
        self.btn_cambiarEstado.setText(QCoreApplication.translate("AltaBajaCarrera", u"Activar/Desactivar", None))
    # retranslateUi

