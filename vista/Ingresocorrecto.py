from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class IngresoCorrecto(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Ingresocorrecto.ui",self)