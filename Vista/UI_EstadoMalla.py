# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alta_baja_malla.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Vista import resources

class Ui_EstadoMalla(object):
    def setupUi(self, EliminarMalla):
        if not EliminarMalla.objectName():
            EliminarMalla.setObjectName(u"EliminarMalla")
        EliminarMalla.setWindowModality(Qt.ApplicationModal)
        EliminarMalla.resize(572, 285)
        EliminarMalla.setMinimumSize(QSize(500, 270))
        EliminarMalla.setMaximumSize(QSize(3000, 3000))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        EliminarMalla.setWindowIcon(icon)
        EliminarMalla.setStyleSheet(u"QWidget{\n"
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
        self.label = QLabel(EliminarMalla)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 572, 51))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 25 16pt \"Microsoft YaHei UI Light\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(EliminarMalla)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 60, 451, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.btn_buscar = QPushButton(self.gridLayoutWidget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setMinimumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-paper-plane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_buscar, 0, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.txt_codmalla = QLineEdit(self.gridLayoutWidget)
        self.txt_codmalla.setObjectName(u"txt_codmalla")
        self.txt_codmalla.setEnabled(True)
        self.txt_codmalla.setMinimumSize(QSize(0, 0))
        self.txt_codmalla.setMaximumSize(QSize(295, 16777215))
        self.txt_codmalla.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_codmalla, 0, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.lbl_promocion = QLabel(self.gridLayoutWidget)
        self.lbl_promocion.setObjectName(u"lbl_promocion")

        self.gridLayout.addWidget(self.lbl_promocion, 3, 1, 1, 1)

        self.lbl_facultad = QLabel(self.gridLayoutWidget)
        self.lbl_facultad.setObjectName(u"lbl_facultad")

        self.gridLayout.addWidget(self.lbl_facultad, 1, 1, 1, 1)

        self.lbl_carrera = QLabel(self.gridLayoutWidget)
        self.lbl_carrera.setObjectName(u"lbl_carrera")

        self.gridLayout.addWidget(self.lbl_carrera, 2, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.lbl_modalidad = QLabel(self.gridLayoutWidget)
        self.lbl_modalidad.setObjectName(u"lbl_modalidad")

        self.gridLayout.addWidget(self.lbl_modalidad, 4, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)

        self.btn_altabaja = QPushButton(EliminarMalla)
        self.btn_altabaja.setObjectName(u"btn_altabaja")
        self.btn_altabaja.setEnabled(False)
        self.btn_altabaja.setGeometry(QRect(210, 230, 151, 41))
        self.btn_altabaja.setMinimumSize(QSize(116, 32))

        self.retranslateUi(EliminarMalla)

        QMetaObject.connectSlotsByName(EliminarMalla)
    # setupUi

    def retranslateUi(self, EliminarMalla):
        EliminarMalla.setWindowTitle(QCoreApplication.translate("EliminarMalla", u"Eliminar Malla", None))
        self.label.setText(QCoreApplication.translate("EliminarMalla", u"Activar/Desactivar Malla", None))
        self.label_2.setText(QCoreApplication.translate("EliminarMalla", u"Facultad", None))
        self.btn_buscar.setText("")
        self.label_12.setText(QCoreApplication.translate("EliminarMalla", u"Carrera", None))
        self.label_13.setText(QCoreApplication.translate("EliminarMalla", u"Promocion", None))
        self.lbl_promocion.setText("")
        self.lbl_facultad.setText("")
        self.lbl_carrera.setText("")
        self.label_11.setText(QCoreApplication.translate("EliminarMalla", u"Codigo Carrera", None))
        self.lbl_modalidad.setText("")
        self.label_14.setText(QCoreApplication.translate("EliminarMalla", u"Modalidad", None))
        self.btn_altabaja.setText(QCoreApplication.translate("EliminarMalla", u"Activar/Desactivar Malla", None))
    # retranslateUi

