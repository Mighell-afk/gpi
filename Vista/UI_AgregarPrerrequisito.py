# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregar_prerrequisitos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Vista import resources

class Ui_CargarPrerrequisito(object):
    def setupUi(self, CargarPrerrequisito):
        if not CargarPrerrequisito.objectName():
            CargarPrerrequisito.setObjectName(u"CargarPrerrequisito")
        CargarPrerrequisito.setWindowModality(Qt.ApplicationModal)
        CargarPrerrequisito.resize(720, 536)
        CargarPrerrequisito.setMinimumSize(QSize(420, 270))
        CargarPrerrequisito.setMaximumSize(QSize(3000, 3000))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        CargarPrerrequisito.setWindowIcon(icon)
        CargarPrerrequisito.setStyleSheet(u"QWidget{\n"
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
        self.label = QLabel(CargarPrerrequisito)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 720, 60))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 25 16pt \"Microsoft YaHei UI Light\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(CargarPrerrequisito)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(180, 70, 361, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cbo_facultad = QComboBox(self.gridLayoutWidget)
        self.cbo_facultad.setObjectName(u"cbo_facultad")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_facultad.sizePolicy().hasHeightForWidth())
        self.cbo_facultad.setSizePolicy(sizePolicy)
        self.cbo_facultad.setMaximumSize(QSize(295, 16777215))
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

        self.gridLayout.addWidget(self.cbo_facultad, 0, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.cbo_materia = QComboBox(self.gridLayoutWidget)
        self.cbo_materia.setObjectName(u"cbo_materia")
        self.cbo_materia.setStyleSheet(u"/* ----------------- QComboBox ----------------- */\n"
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

        self.gridLayout.addWidget(self.cbo_materia, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(CargarPrerrequisito)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(220, 210, 281, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_Anadir = QPushButton(self.horizontalLayoutWidget)
        self.btn_Anadir.setObjectName(u"btn_Anadir")
        self.btn_Anadir.setMinimumSize(QSize(116, 32))

        self.horizontalLayout.addWidget(self.btn_Anadir)

        self.btn_Eliminar = QPushButton(self.horizontalLayoutWidget)
        self.btn_Eliminar.setObjectName(u"btn_Eliminar")
        self.btn_Eliminar.setMinimumSize(QSize(116, 32))

        self.horizontalLayout.addWidget(self.btn_Eliminar)

        self.table_prerrequisito = QTableWidget(CargarPrerrequisito)
        self.table_prerrequisito.setObjectName(u"table_prerrequisito")
        self.table_prerrequisito.setGeometry(QRect(10, 300, 701, 221))

        self.retranslateUi(CargarPrerrequisito)

        QMetaObject.connectSlotsByName(CargarPrerrequisito)
    # setupUi

    def retranslateUi(self, CargarPrerrequisito):
        CargarPrerrequisito.setWindowTitle(QCoreApplication.translate("CargarPrerrequisito", u"Agregar Prerrequisito", None))
        self.label.setText(QCoreApplication.translate("CargarPrerrequisito", u"Agregar Prerrequisitos", None))
        self.label_10.setText(QCoreApplication.translate("CargarPrerrequisito", u"Facultad", None))
        self.label_8.setText(QCoreApplication.translate("CargarPrerrequisito", u"Materia", None))
        self.btn_Anadir.setText(QCoreApplication.translate("CargarPrerrequisito", u"A\u00f1adir", None))
        self.btn_Eliminar.setText(QCoreApplication.translate("CargarPrerrequisito", u"Eliminar", None))
    # retranslateUi

