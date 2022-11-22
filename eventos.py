from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import *

def InfoMsg(self,title,text):
    self.msgBox = QMessageBox()
    self.msgBox.setText(f"{text}")
    self.msgBox.setWindowTitle(f"{title}")
    self.msgBox.setIcon(QMessageBox.Information)
    self.msgBox.setStandardButtons(QMessageBox.Ok)
    self.msgBox.exec_()
    
def WarningMsg(self,title,text):
    self.msgBox = QMessageBox()
    self.msgBox.setText(f"{text}")
    self.msgBox.setWindowTitle(f"{title}")
    self.msgBox.setIcon(QMessageBox.Warning)
    self.msgBox.setStandardButtons(QMessageBox.Ok)
    self.msgBox.exec_()

def CritiCalMsg(self,title,text):
    self.msgBox = QMessageBox()
    self.msgBox.setText(f"{text}")
    self.msgBox.setWindowTitle(f"{title}")
    self.msgBox.setIcon(QMessageBox.Critical)
    self.msgBox.setStandardButtons(QMessageBox.Ok)
    self.msgBox.exec_()