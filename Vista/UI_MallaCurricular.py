# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'malla_curricular.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Vista import resources

class Ui_MallaCurricular(object):
    def setupUi(self, MallaCurricular):
        if not MallaCurricular.objectName():
            MallaCurricular.setObjectName(u"MallaCurricular")
        MallaCurricular.resize(1280, 816)
        MallaCurricular.setMinimumSize(QSize(1280, 720))
        icon = QIcon()
        icon.addFile(u":/images/images/images/Logo_vertical.png", QSize(), QIcon.Normal, QIcon.Off)
        MallaCurricular.setWindowIcon(icon)
        self.styleSheet = QWidget(MallaCurricular)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: #333;\n"
"	font: 9pt \"Segoe UI\";\n"
"}\n"
"/* -----------------  MENUS ----------------- */\n"
"\n"
"\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	"
                        "color: rgb(255, 255, 255);\n"
"}\n"
"/* ----------------- Bottom Bar ----------------- */\n"
"/*Status bar (inferior)*/\n"
"#bottomBar { background-color: #2A3C57 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"\n"
"/* ----------------- QTableWidget ----------------- */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"/*	padding: 10px;*/\n"
"	border-radius: 5px;\n"
"	gridline-color: #6C99DD;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: tranparent;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: transparent;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"	background-color:#6C99DD; /*color al seleccionar el cuadro*/\n"
"    color: white;/*color de la letra en el cuadro*/\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: white;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"\n"
"/*\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
""
                        "}\n"
"*/\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #1F54A3;\n"
"	background-color: #1F54A3;\n"
"/*	padding: 3px;*/\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #1F54A3;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"	padding-left:4px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
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
"\n"
"/* ----------------- ScrollBars ----------------- */\n"
"/*tama\u00f1o y bordes*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    "
                        "height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"/*la linea*/\n"
"QScrollBar::handle:horizontal {\n"
"    background: #296FD6;\n"
"    min-width: 25px;\n"
"\n"
"}\n"
"/*bordecito inferior derecho*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #102D57;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"/*bordecito inferior izquierdo*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #102D57;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*tama\u00f1o y bordes*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"/*la linea*/\n"
" QScrollBar::han"
                        "dle:vertical {	\n"
"	background: #296FD6;\n"
"    min-height: 25px;\n"
"\n"
" }\n"
"/*bordecito lateral inferior*/\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #102D57;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"/*bordecito lateral superior*/\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #102D57;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"/* ----------------- RadioButton ----------------- */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #102D57;\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	border-radius: 9px;\n"
"    background: #102D57;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid #1F54A3;\n"
"}\n"
"\n"
"QRadioButton::indicator:checke"
                        "d {\n"
"    background: 3px solid #296FD6;\n"
"	border: 3px solid #296FD6;	\n"
"}\n"
"/* ----------------- QComboBox ----------------- */\n"
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
"\n"
"\n"
"\n"
"")
        self.gridLayout_10 = QGridLayout(self.styleSheet)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.groupBox_5 = QGroupBox(self.pagesContainer)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.txt_buscar_mallla = QLineEdit(self.groupBox_5)
        self.txt_buscar_mallla.setObjectName(u"txt_buscar_mallla")

        self.horizontalLayout_20.addWidget(self.txt_buscar_mallla)


        self.horizontalLayout_19.addWidget(self.groupBox_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.btn_ver_malla = QPushButton(self.pagesContainer)
        self.btn_ver_malla.setObjectName(u"btn_ver_malla")
        self.btn_ver_malla.setMinimumSize(QSize(100, 30))
        self.btn_ver_malla.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_ver_malla)

        self.btn_agregar = QPushButton(self.pagesContainer)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setMinimumSize(QSize(100, 30))
        self.btn_agregar.setFocusPolicy(Qt.TabFocus)
        self.btn_agregar.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_agregar)

        self.btn_modificar = QPushButton(self.pagesContainer)
        self.btn_modificar.setObjectName(u"btn_modificar")
        self.btn_modificar.setMinimumSize(QSize(100, 30))
        self.btn_modificar.setFocusPolicy(Qt.TabFocus)
        self.btn_modificar.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_modificar)

        self.btn_eliminar = QPushButton(self.pagesContainer)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setMinimumSize(QSize(100, 30))
        self.btn_eliminar.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_eliminar)

        self.btn_baja = QPushButton(self.pagesContainer)
        self.btn_baja.setObjectName(u"btn_baja")
        self.btn_baja.setMinimumSize(QSize(150, 30))
        self.btn_baja.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_baja)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)

        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.personas = QWidget()
        self.personas.setObjectName(u"personas")
        self.gridLayout_8 = QGridLayout(self.personas)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.rdb_activo = QRadioButton(self.personas)
        self.rdb_activo.setObjectName(u"rdb_activo")

        self.horizontalLayout.addWidget(self.rdb_activo)

        self.rdb_inactivo = QRadioButton(self.personas)
        self.rdb_inactivo.setObjectName(u"rdb_inactivo")

        self.horizontalLayout.addWidget(self.rdb_inactivo)

        self.rdb_all = QRadioButton(self.personas)
        self.rdb_all.setObjectName(u"rdb_all")

        self.horizontalLayout.addWidget(self.rdb_all)

        self.btn_filtrar = QPushButton(self.personas)
        self.btn_filtrar.setObjectName(u"btn_filtrar")
        self.btn_filtrar.setMinimumSize(QSize(100, 30))
        self.btn_filtrar.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid #1F54A3;\n"
"	border-radius: 5px;	\n"
"	background-color: #1F54A3;\n"
"	color:white;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #286FD6;\n"
"	border: 2px solid #286FD6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #2A3C57;\n"
"	border: 2px solid #2A3C57;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_filtrar)


        self.gridLayout_8.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.table_mallas = QTableWidget(self.personas)
        self.table_mallas.setObjectName(u"table_mallas")
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(51, 51, 51, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(51, 51, 51, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(51, 51, 51, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.table_mallas.setPalette(palette)
        self.table_mallas.setStyleSheet(u"QTableWidget{\n"
"	background-color: #ffffff;\n"
"}")

        self.gridLayout_8.addWidget(self.table_mallas, 3, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")

        self.gridLayout_8.addLayout(self.gridLayout_13, 1, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")

        self.gridLayout_8.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.personas)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fechahora = QLabel(self.bottomBar)
        self.fechahora.setObjectName(u"fechahora")
        self.fechahora.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.fechahora)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_10.addWidget(self.bgApp, 0, 0, 1, 1)

        MallaCurricular.setCentralWidget(self.styleSheet)

        self.retranslateUi(MallaCurricular)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MallaCurricular)
    # setupUi

    def retranslateUi(self, MallaCurricular):
        MallaCurricular.setWindowTitle(QCoreApplication.translate("MallaCurricular", u"Malla Curricular", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MallaCurricular", u"Buscar", None))
        self.txt_buscar_mallla.setPlaceholderText(QCoreApplication.translate("MallaCurricular", u"Buscar...", None))
        self.btn_ver_malla.setText(QCoreApplication.translate("MallaCurricular", u"Ver Malla Curricular", None))
#if QT_CONFIG(tooltip)
        self.btn_agregar.setToolTip(QCoreApplication.translate("MallaCurricular", u"Agregar Malla Curricular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_agregar.setText(QCoreApplication.translate("MallaCurricular", u"Agregar", None))
#if QT_CONFIG(tooltip)
        self.btn_modificar.setToolTip(QCoreApplication.translate("MallaCurricular", u"Modificar Malla Curricular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_modificar.setText(QCoreApplication.translate("MallaCurricular", u"Modificar", None))
#if QT_CONFIG(tooltip)
        self.btn_eliminar.setToolTip(QCoreApplication.translate("MallaCurricular", u"EliminarMallaCurricular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_eliminar.setText(QCoreApplication.translate("MallaCurricular", u"Eliminar", None))
        self.btn_baja.setText(QCoreApplication.translate("MallaCurricular", u"Activar/Desactivar", None))
        self.rdb_activo.setText(QCoreApplication.translate("MallaCurricular", u"Mostrar activos", None))
        self.rdb_inactivo.setText(QCoreApplication.translate("MallaCurricular", u"Mostrar inactivos", None))
        self.rdb_all.setText(QCoreApplication.translate("MallaCurricular", u"Mostrar todos", None))
        self.btn_filtrar.setText(QCoreApplication.translate("MallaCurricular", u"Filtrar", None))
        self.fechahora.setText("")
    # retranslateUi

