from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class Validacion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("FaltaCampo2.ui",self)