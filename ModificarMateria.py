from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys
from conexion import BaseDeDatos
from Vista.ui_modificarMateria import Ui_MdificarMateria
from eventos import *

class ModificarMateria(QtWidgets.QMainWindow):
   
    

    def __init__(self,parent = None):
        super().__init__(parent)
        self.modmateria = Ui_MdificarMateria()
        self.modmateria.setupUi(self)
        self.parent = parent
        self.QueryCombo = "SELECT idfacultad,nombre,siglas FROM facultad where activo = 1"
        self.modmateria.btn_buscar.clicked.connect(lambda:self.ObtenerDatos())
        self.modmateria.btn_modificar.clicked.connect(lambda:self.ActualizarDatos())

    
    def ObtenerDatos(self):
        if self.ValidarFacultad():
            global DatosMateria
            self.connect = BaseDeDatos()
            self.con = self.connect.con
            self.cur = self.con.cursor()
            id = self.modmateria.txt_codMateria.text()
            # self.cur.execute(f"SELECT idMateria,Facultad_ID,Nombre FROM materia where idMateria = {int(id)} and Activo = 1;")
            self.cur.execute(f"select idMateria,mt.Nombre as Materia,fa.nombre as facultad from materia mt INNER JOIN facultad fa on (mt.idfacultad = fa.idfacultad) WHERE idMateria ={int(id)} and mt.Activo =1; ")
            DatosMateria = self.cur.fetchall()
    
            if DatosMateria != []:
                self.modmateria.txt_nombreMateria.setText(str(DatosMateria[0][1]))
                self.CargarFacultad()
                self.HabilitarCampos(True)
            else:
                WarningMsg(self,"Atencion","Codigo de la materia no existe")
                

    def CargarFacultad(self):
        
        global id
        self.connect = BaseDeDatos()
        self.con = self.connect.con
        self.cur = self.con.cursor()
        self.cur.execute(self.QueryCombo)
        allfacus = []
        DatosFacultad = self.cur.fetchall()
        for i in range(len(DatosFacultad)):
            Data = DatosFacultad[i][1] +" - "+ DatosFacultad[i][2]
            id = DatosFacultad[i][0]
            self.modmateria.cbo_Facultad.addItem(Data,str(id))
            allfacus.append(DatosFacultad[i][1])
        #poner el que cargo el usuario
        self.modmateria.cbo_Facultad.findText(str(DatosMateria[0][2]),Qt.MatchFixedString)
        index = 0
        for i in range(len(allfacus)):
            if allfacus[i] == DatosMateria[0][2]:
                break
            else:
                index += 1 
        self.modmateria.cbo_Facultad.setCurrentIndex(index)
        

    def ValidarFacultad(self):
        codMateria = self.modmateria.txt_codMateria.text()
    
        if not codMateria.isnumeric() or codMateria == "":
            WarningMsg(self,"Atencion","Codigo de la materia no es numerico")
            return False

        return True

    def ActualizarDatos(self):
        
        FacuID = self.modmateria.cbo_Facultad.currentData()
        NombreMate = self.modmateria.txt_nombreMateria.text()
        if NombreMate != "":
            self.cur.execute(f" UPDATE materia SET idfacultad = {FacuID}, Nombre = '{NombreMate}' WHERE idMateria = {int(DatosMateria[0][0])} ")
            self.con.commit()
            self.LimpiarCampos()
            InfoMsg(self,'Informacion','Materia Modificada con exito')
            self.parent.ActualizarMateria(self.parent.QueryForActive)
        else:
            WarningMsg(self,'Atencion','Ingrese el nombre de la materia')


    def LimpiarCampos(self):
        self.HabilitarCampos(False)
        self.modmateria.txt_nombreMateria.clear()
        self.modmateria.cbo_Facultad.setCurrentIndex(-1)
        self.modmateria.txt_codMateria.clear()


            
    def HabilitarCampos(self,state):
        self.modmateria.txt_nombreMateria.setEnabled(state)
        self.modmateria.cbo_Facultad.setEnabled(state)
        self.modmateria.btn_modificar.setEnabled(state)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_aplicacion = ModificarMateria()
    mi_aplicacion.show()
    sys.exit(app.exec_())
