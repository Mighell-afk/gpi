# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ver_malla.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Vista import resources

class Ui_VerMalla(object):
    def setupUi(self, AgregarMalla):
        if not AgregarMalla.objectName():
            AgregarMalla.setObjectName(u"AgregarMalla")
        AgregarMalla.setWindowModality(Qt.ApplicationModal)
        AgregarMalla.resize(849, 571)
        AgregarMalla.setMinimumSize(QSize(500, 270))
        AgregarMalla.setMaximumSize(QSize(3000, 3000))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        AgregarMalla.setWindowIcon(icon)
        AgregarMalla.setStyleSheet(u"QWidget{\n"
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
        self.label = QLabel(AgregarMalla)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 850, 60))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 25 16pt \"Microsoft YaHei UI Light\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(AgregarMalla)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 70, 771, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_promocion = QLineEdit(self.gridLayoutWidget)
        self.txt_promocion.setObjectName(u"txt_promocion")
        self.txt_promocion.setEnabled(False)
        self.txt_promocion.setMinimumSize(QSize(0, 0))
        self.txt_promocion.setMaximumSize(QSize(295, 16777215))
        self.txt_promocion.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_promocion, 0, 3, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)

        self.txt_cod_malla = QLineEdit(self.gridLayoutWidget)
        self.txt_cod_malla.setObjectName(u"txt_cod_malla")
        self.txt_cod_malla.setEnabled(False)
        self.txt_cod_malla.setMinimumSize(QSize(0, 0))
        self.txt_cod_malla.setMaximumSize(QSize(295, 16777215))
        self.txt_cod_malla.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_cod_malla, 0, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.txt_ano_inicio = QLineEdit(self.gridLayoutWidget)
        self.txt_ano_inicio.setObjectName(u"txt_ano_inicio")
        self.txt_ano_inicio.setEnabled(False)
        self.txt_ano_inicio.setMinimumSize(QSize(0, 0))
        self.txt_ano_inicio.setMaximumSize(QSize(295, 16777215))
        self.txt_ano_inicio.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_ano_inicio, 1, 3, 1, 1)

        self.txt_modalidad = QLineEdit(self.gridLayoutWidget)
        self.txt_modalidad.setObjectName(u"txt_modalidad")
        self.txt_modalidad.setEnabled(False)
        self.txt_modalidad.setMinimumSize(QSize(0, 0))
        self.txt_modalidad.setMaximumSize(QSize(295, 16777215))
        self.txt_modalidad.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_modalidad, 3, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)

        self.txt_carrera = QLineEdit(self.gridLayoutWidget)
        self.txt_carrera.setObjectName(u"txt_carrera")
        self.txt_carrera.setEnabled(False)
        self.txt_carrera.setMinimumSize(QSize(0, 0))
        self.txt_carrera.setMaximumSize(QSize(295, 16777215))
        self.txt_carrera.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_carrera, 2, 1, 1, 1)

        self.txt_facultad = QLineEdit(self.gridLayoutWidget)
        self.txt_facultad.setObjectName(u"txt_facultad")
        self.txt_facultad.setEnabled(False)
        self.txt_facultad.setMinimumSize(QSize(0, 0))
        self.txt_facultad.setMaximumSize(QSize(295, 16777215))
        self.txt_facultad.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_facultad, 1, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 1, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.txt_duracion = QLineEdit(self.gridLayoutWidget)
        self.txt_duracion.setObjectName(u"txt_duracion")
        self.txt_duracion.setEnabled(False)
        self.txt_duracion.setMinimumSize(QSize(0, 0))
        self.txt_duracion.setMaximumSize(QSize(295, 16777215))
        self.txt_duracion.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_duracion, 3, 3, 1, 1)

        self.txt_fecha_inicio = QLineEdit(self.gridLayoutWidget)
        self.txt_fecha_inicio.setObjectName(u"txt_fecha_inicio")
        self.txt_fecha_inicio.setEnabled(False)
        self.txt_fecha_inicio.setMinimumSize(QSize(0, 0))
        self.txt_fecha_inicio.setMaximumSize(QSize(295, 16777215))
        self.txt_fecha_inicio.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.txt_fecha_inicio, 2, 3, 1, 1)

        self.table_materia = QTableWidget(AgregarMalla)
        self.table_materia.setObjectName(u"table_materia")
        self.table_materia.setGeometry(QRect(20, 280, 811, 220))
        self.table_materia.setMinimumSize(QSize(0, 0))
        self.table_materia.setMaximumSize(QSize(970, 220))
        self.btn_ver_prerrequisito = QPushButton(AgregarMalla)
        self.btn_ver_prerrequisito.setObjectName(u"btn_ver_prerrequisito")
        self.btn_ver_prerrequisito.setGeometry(QRect(360, 520, 131, 30))
        self.btn_ver_prerrequisito.setMinimumSize(QSize(100, 30))
        self.btn_ver_prerrequisito.setMaximumSize(QSize(200, 30))

        self.retranslateUi(AgregarMalla)

        QMetaObject.connectSlotsByName(AgregarMalla)
    # setupUi

    def retranslateUi(self, AgregarMalla):
        AgregarMalla.setWindowTitle(QCoreApplication.translate("AgregarMalla", u"Ver Malla", None))
        self.label.setText(QCoreApplication.translate("AgregarMalla", u"Malla", None))
        self.label_15.setText(QCoreApplication.translate("AgregarMalla", u"Codigo Malla", None))
        self.label_13.setText(QCoreApplication.translate("AgregarMalla", u"Fecha de inicio", None))
        self.label_10.setText(QCoreApplication.translate("AgregarMalla", u"Promocion", None))
        self.label_11.setText(QCoreApplication.translate("AgregarMalla", u"Facultad", None))
        self.label_14.setText(QCoreApplication.translate("AgregarMalla", u"Duracion", None))
        self.label_16.setText(QCoreApplication.translate("AgregarMalla", u"A\u00f1o de inicio", None))
        self.label_12.setText(QCoreApplication.translate("AgregarMalla", u"Modalidad", None))
        self.label_8.setText(QCoreApplication.translate("AgregarMalla", u"Carrera", None))
        self.btn_ver_prerrequisito.setText(QCoreApplication.translate("AgregarMalla", u"Ver Prerrequisitos", None))
    # retranslateUi

