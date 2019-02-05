# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejecu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import vista
from vista.ValidacionEquipo1 import Dialog
from vista.ValidacionEquipo2 import Validacion
from vista.ValidarMonto import ValidacionMonto
from vista.Ingresocorrecto import IngresoCorrecto
import time
import os.path as path
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ecuavoley-Project 2.0")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnImagenPantalla = QtWidgets.QPushButton(self.centralwidget)
        self.btnImagenPantalla.setGeometry(QtCore.QRect(0, -50, 801, 441))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.btnImagenPantalla.setPalette(palette)
        self.btnImagenPantalla.setAutoFillBackground(False)
        self.btnImagenPantalla.setText("")
        icon = QtGui.QIcon()
        #Insertamos el path para agregar la imagen al window
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/Ecuavoley mi mundo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImagenPantalla.setIcon(icon)
        self.btnImagenPantalla.setIconSize(QtCore.QSize(1200, 350))
        self.btnImagenPantalla.setObjectName("btnImagenPantalla")
        self.cmbModalidad = QtWidgets.QComboBox(self.centralwidget)
        self.cmbModalidad.setGeometry(QtCore.QRect(100, 300, 111, 22))
        self.cmbModalidad.setObjectName("cmbModalidad")
        self.txtJugador1 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtJugador1.setEnabled(True)
        self.txtJugador1.setGeometry(QtCore.QRect(120, 130, 131, 31))
        self.txtJugador1.setObjectName("txtJugador1")
        self.lblMonto = QtWidgets.QLabel(self.centralwidget)
        self.lblMonto.setGeometry(QtCore.QRect(540, 310, 47, 13))
        self.lblMonto.setObjectName("lblMonto")
        self.lblModalidad = QtWidgets.QLabel(self.centralwidget)
        self.lblModalidad.setGeometry(QtCore.QRect(30, 300, 61, 20))
        self.lblModalidad.setObjectName("lblModalidad")
        self.txtMonto = QtWidgets.QTextEdit(self.centralwidget)
        self.txtMonto.setGeometry(QtCore.QRect(590, 300, 81, 31))
        self.txtMonto.setObjectName("txtMonto")
        self.lblJugador1 = QtWidgets.QLabel(self.centralwidget)
        self.lblJugador1.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.lblJugador1.setObjectName("lblJugador1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 100, 47, 13))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.txtJugador2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtJugador2.setGeometry(QtCore.QRect(120, 190, 131, 31))
        self.txtJugador2.setObjectName("txtJugador2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 30, 41, 41))
        font = QtGui.QFont()

        #Se coloca un estilo de tipo de letra para la interfaz.
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblJugador3_T2 = QtWidgets.QLabel(self.centralwidget)
        self.lblJugador3_T2.setGeometry(QtCore.QRect(480, 250, 47, 13))
        self.lblJugador3_T2.setObjectName("lblJugador3_T2")
        self.lblJugador2 = QtWidgets.QLabel(self.centralwidget)
        self.lblJugador2.setGeometry(QtCore.QRect(30, 190, 47, 13))
        self.lblJugador2.setObjectName("lblJugador2")
        self.txtJugador1_T2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtJugador1_T2.setGeometry(QtCore.QRect(590, 130, 131, 31))
        self.txtJugador1_T2.setObjectName("txtJugador1_T2")
        self.txtJugador2_T2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtJugador2_T2.setGeometry(QtCore.QRect(590, 190, 131, 31))
        self.txtJugador2_T2.setObjectName("txtJugador2_T2")
        self.txtJugador3 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtJugador3.setGeometry(QtCore.QRect(120, 250, 131, 31))
        self.txtJugador3.setObjectName("txtJugador3")
        self.lblJugador2_T2 = QtWidgets.QLabel(self.centralwidget)
        self.lblJugador2_T2.setGeometry(QtCore.QRect(480, 190, 47, 13))
        self.lblJugador2_T2.setObjectName("lblJugador2_T2")
        self.lblJugador3 = QtWidgets.QLabel(self.centralwidget)
        self.lblJugador3.setGeometry(QtCore.QRect(30, 250, 47, 13))
        self.lblJugador3.setObjectName("lblJugador3")
        self.lblJugador1_T2 = QtWidgets.QLabel(self.centralwidget)
        self.lblJugador1_T2.setGeometry(QtCore.QRect(480, 130, 47, 13))
        self.lblJugador1_T2.setObjectName("lblJugador1_T2")
        self.txtJugador3_T2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtJugador3_T2.setGeometry(QtCore.QRect(590, 250, 131, 31))
        self.txtJugador3_T2.setObjectName("txtJugador3_T2")
        self.txtPartidos = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPartidos.setGeometry(QtCore.QRect(0, 340, 801, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 121, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 130, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 121, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 130, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)

        #Palette nos permite cambiar el color del texto o ventanas.
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 130, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.txtPartidos.setPalette(palette)
        self.txtPartidos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.txtPartidos.setObjectName("txtPartidos")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(390, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        font.setItalic(True)
        self.btnGuardar.setFont(font)
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnVerPartidos = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerPartidos.setGeometry(QtCore.QRect(290, 540, 51, 41))
        self.btnVerPartidos.setText("")
        icon1 = QtGui.QIcon()

        #Aqui agregamos la imagen que se requiera, colocando el path de la imagen
        icon1.addPixmap(QtGui.QPixmap("../../../Desktop/ecuavoley balon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVerPartidos.setIcon(icon1)
        self.btnVerPartidos.setIconSize(QtCore.QSize(150, 40))
        self.btnVerPartidos.setObjectName("btnVerPartidos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Añadimos los items para la modalidad de los partidos
        self.cmbModalidad.addItem("RAQUETA")
        self.cmbModalidad.addItem("PIE CABEZA")
        self.cmbModalidad.addItem("GANCHO TECNICO")
        self.cmbModalidad.addItem("COLOQUE")
        self.cmbModalidad.addItem("GANCHO")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #Ventana Principal del Proyecto
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Ecuavoley 2.0"))

        #Variables (labels,textfields,pushbuttons)
        self.lblMonto.setText(_translate("MainWindow", "Monto: $"))
        self.lblModalidad.setText(_translate("MainWindow", "Modalidad:"))
        self.lblJugador1.setText(_translate("MainWindow", "Jugador 1"))
        self.label.setText(_translate("MainWindow", "Equipo 1"))
        self.label_3.setText(_translate("MainWindow", "Equipo 2"))
        self.label_2.setText(_translate("MainWindow", "VS"))
        self.lblJugador3_T2.setText(_translate("MainWindow", "Jugador 3"))
        self.lblJugador2.setText(_translate("MainWindow", "Jugador 2"))
        self.lblJugador2_T2.setText(_translate("MainWindow", "Jugador 2"))
        self.lblJugador3.setText(_translate("MainWindow", "Jugador 3"))
        self.lblJugador1_T2.setText(_translate("MainWindow", "Jugador 1"))
        self.btnGuardar.setText(_translate("MainWindow", "Registrar  ✔"))


        #Eventos de los pushbuttons (btnVerPartidos y Guardar)
        self.btnVerPartidos.clicked.connect(self.datosPartido)
        self.btnGuardar.clicked.connect(self.guardar)


        #Creacion de variables para poder llamar a ventanas
        #de validacion de datos escritos incorrectamente.
        self.equipo1=Dialog()
        self.equipo2=Validacion()
        self.monto=ValidacionMonto()
        self.ingreso=IngresoCorrecto()

    #Metodo que permite desplegar la informacion de los partidos en el txtPartidos
    def datosPartido(self):

            arch = open(r"C:\Users\user\Desktop\Ecuavoley\partidos.txt", "r") #Abrir un archivo
            lec = arch.readlines() # Leer todas las lineas del archivo "PARTIDOS.txt"
            guardar = ""

            #Ciclo for que permite almacenar la informacion del archivo .txt para desplegar en pantalla
            for line in lec:
                guardar += line + "\n"

            self.txtPartidos.setText(guardar) #Aqui seteamos la variable txt por la informacion guardada
            arch.close() #Cerramos el archivo txt abierto.


    #Metodo que sirve para registrar partidos y verificar si existen errores para registrar un partido.
    def guardar(self):
        validar=1

        #Es conveniente utilizar un try - except por cualquier error
        #que pueda surgir en la transformacion o captura de datos.

        try:

         if(self.txtJugador1.toPlainText()=="" and self.txtJugador2.toPlainText()=="" and self.txtJugador3.toPlainText()==""):
            self.equipo1.exec_()  #Se muestra una ventana por el error cometido
            validar=0
         if (self.txtJugador1_T2.toPlainText() == "" and self.txtJugador2_T2.toPlainText() == "" and self.txtJugador3_T2.toPlainText() == ""):
          self.equipo2.exec_() #Se muestra una ventana por el error cometido
          validar=0

         monto=int(self.txtMonto.toPlainText())

         if(monto<0):
             self.monto.exec_()  #Se muestra una ventana por el error cometido
             validar=0
             print("Menor")
         else:
             print("Mayor")
        except:
             self.monto.exec_() #Se muestra una ventana por el error cometido
             validar = 0


        #Verificamos si anteriormente se cometió algun error en el ingreso de datos
        #si la variable es 1, fue correcto el ingreso y se procederá a registrar
        #caso contrario enviará mensajes de error donde el usuario cometió la equivocacion.

        #try:
        if(validar==1):
            archivo_partidos = open(r"C:\Users\user\Desktop\Ecuavoley\partidos.txt", "a")
            archivo_partidos.write(
                "PARTIDO-->    MODALIDAD: " + self.cmbModalidad.currentText() + "\t\t\tHora:" + time.strftime(
                    "%X") + "\n")
            archivo_partidos.write("EQUIPO 1\t\t\t\tEquipo 2\n")
            archivo_partidos.write(
                self.txtJugador1.toPlainText() + "\t\t\t\t" + self.txtJugador1_T2.toPlainText() + "\n")
            archivo_partidos.write(
                self.txtJugador2.toPlainText() + "\t\t\t\t" + self.txtJugador2_T2.toPlainText() + "\n")
            archivo_partidos.write(
                self.txtJugador3.toPlainText() + "\t\t\t\t" + self.txtJugador3_T2.toPlainText() + "\n")
            archivo_partidos.write("\t\t\t\t\t\tMonto: $ " + self.txtMonto.toPlainText() + "\n")
            archivo_partidos.write(
                "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            archivo_partidos.close()


            #Verificamos si el archivo existe para guardar la informacion de la ganancia
            # respectiva para la cancha

            # "r" se coloca debio a que la lectura del path se pone sin formato
            # debido a esto nos ayuda evitando errores.
            if path.exists(r"C:\Users\user\Desktop\Ecuavoley\ganancias.txt"):

                registro = open(r"C:\Users\user\Desktop\Ecuavoley\ganancias.txt", "r")
                val = registro.readlines()

                for line in val:  #Con el ciclo for obtenemos el valor que se
                    valor = line  #encontraba en el archivo


                registro.close() # cerramos el archivo

                #abrimos el archivo en modo escritura para guardar el nuevo valor
                registro = open(r"C:\Users\user\Desktop\Ecuavoley\ganancias.txt", "w")
                porce = float(self.txtMonto.toPlainText())*.10
                nuevo_valor = float(float(valor) + (porce/2))
                registro.write(str(nuevo_valor))

                registro.close()  # cerramos el archivo

            else:
                #En caso de que el archivo no exista, se lo crea y se escribe
                #un valor 0 para empezar a generar las ganancias.
                registro = open(r"C:\Users\user\Desktop\Ecuavoley\ganancias.txt", "w")
                registro.write("0") #escribimos el valor 0 en el archivo
                registro.close()  # cerramos el archivo

                #abrimos el archivo en modo de lectura
                registro = open(r"C:\Users\user\Desktop\Ecuavoley\ganancias.txt", "r")
                val = registro.readlines()

                for line in val:
                    valor = line #guardamos en una variable el valor del archivo
                registro.close()  # cerramos el archivo

                # abrimos el archivo en modo escritura para actualizar el nuevo valor.
                registro = open(r"C:\Users\user\Desktop\Ecuavoley\ganancias.txt", "w")
                porce = float(self.txtMonto.toPlainText()) * .10 # calculamos el porcentaje de ganancia

                #EL PORCENTAJE PUEDE VARIAR DEPENDIENDO COMO SE MANEJE LA GANANCIA DE LA CANCHA
                #EN ESTE CASO SE APLICA EL 10% DEL MONTO A JUGARSE
                #DEL 10% SE REPARTE LA MITAD (PARA EL JUEZ Y LA CANCHA)
                #EL VALOR QUE SE REGISTRA ES UNICAMENTE EL DE LA CANCHA, PORQUE NOS
                #INTERESA SABER CUANTO GANÓ LA CANCHA

                nuevo_valor = float(float(valor) + (porce / 2))
                registro.write(str(nuevo_valor))

                registro.close()  # cerramos el archivo



            #Seteo de los txt para un el ingreso de un nuevo registro
            #asi el usuario no tiene que borrar los campos
            self.txtMonto.setText("")
            self.txtJugador1.setText("")
            self.txtJugador2.setText("")
            self.txtJugador3.setText("")
            self.txtJugador1_T2.setText("")
            self.txtJugador2_T2.setText("")
            self.txtJugador3_T2.setText("")

            #Se muestra un mensaje de ingreso exitoso del partido.
            self.ingreso.exec_()
          #except:
            #print("Error, al actualizar contabilidad.txt")
            #self.nombrevariable.exec_() nos permite llamar a otra ventana y mostrar en pantalla
            #los mensajes respectivos para cada caso.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) #Culminacion de la aplicacion.

