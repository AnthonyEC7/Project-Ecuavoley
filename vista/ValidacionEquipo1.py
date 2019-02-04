from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("FaltaCampo.ui",self)