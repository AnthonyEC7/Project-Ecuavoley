from tkinter import *

ventana = Tk()
colorFondo="#002"
ventana.title("Torneos Ecuavoley")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)
botonAgregar=Button(ventana, text="Agregar Partido").place(x=50,y=200)
botonVer=Button(ventana, text="Ver Partido",command=i).place(x=50,y=250)
mainloop()