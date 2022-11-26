from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import *

def MessageBox(self,title,text):
    self.msgBox = QMessageBox()
    self.msgBox.setText(f"{text}")
    self.msgBox.setWindowTitle(f"{title}")
    self.msgBox.setStandardButtons(QMessageBox.Ok)
    

def InfoMsg(self,title,text):
    MessageBox(self,title,text)
    self.msgBox.setIcon(QMessageBox.Information)
    self.msgBox.exec_()
    
def WarningMsg(self,title,text):
    MessageBox(self,title,text)
    self.msgBox.setIcon(QMessageBox.Warning)
    self.msgBox.exec_()

def CritiCalMsg(self,title,text):
    MessageBox(self,title,text)
    self.msgBox.setIcon(QMessageBox.Critical)
    self.msgBox.exec_()