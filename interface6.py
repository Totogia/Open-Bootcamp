from tkinter import *
from tkinter import ttk
import tkinter


#ventana
ventana = tkinter.Tk()
ventana.title("Catalogo de peliculas")
ventana.geometry ("900x400")
ventana.columnconfigure (0, weight=1)
ventana.columnconfigure (0, weight=7)

#catalogo de peliculas: Harry Potter
Harry_Potter= ttk.Label (ventana, text="Harry Pottter")
Harry_Potter.grid (column = 0, row=0, padx=5, pady=5)
boton = tkinter.Button(ventana, text="Mostrar más información", command=lambda: mostrar_informacion_1())
boton.grid(column = 0, row=1, padx=5, pady=5) 

etiqueta1 = Label(ventana, text="Leer resumen de saga")  
etiqueta1.grid(column = 0, row=2, padx=5, pady=5) 
#----------------------------------------------------------------------------------------------------------
#catalogo de peliculas: Rapido y Furioso
Rapidos_y_Furioso= ttk.Label (ventana, text="Rapido y Furioso")
Rapidos_y_Furioso.grid (column = 4, row=0, padx=5, pady=5)
boton = tkinter.Button(ventana, text="Mostrar más información", command=lambda: mostrar_informacion_2())
boton.grid(column = 4, row=1, padx=5, pady=5) 

etiqueta2 = Label(ventana, text="Leer resumen de saga")  
etiqueta2.grid(column = 4, row=2, padx=5, pady=5) 
 #--------------------------------------------------------------------------------------------------------------------
 #resumen de Harry Potter
def mostrar_informacion_1():  

    etiqueta1.config(text="El día de su cumpleaños,\n Harry Potter descubre que es hijo de dos conocidos hechiceros,\n de los que ha heredado poderes mágicos.\n Debe asistir a una famosa escuela de magia y hechicería,\n donde entabla una amistad con dos jóvenes\n que se convertirán en sus compañeros de aventura.\n Durante su primer año en Hogwarts,\n descubre que un malévolo y poderoso mago llamado Voldemort\n está en busca de una piedra filosofal que alarga la vida de quien la posee.") 

    
    def ocultar_informacion_1():  

        etiqueta1.config(text="")

    Button (ventana, text="ocultar", command=ocultar_informacion_1).grid(column = 0, row=3, padx=5, pady=5)

#--------------------------------------------------------------------------------------------------------------------
#resumen de Rapidos y Furiosos
def mostrar_informacion_2():  

    etiqueta2.config(text="Dominic Toretto (Vin Diesel) conduce por las calles de Los Ángeles\n como si le pertenecieran.\n En lo que respecta a su equipo de gente,\n de hecho le pertenece.\n Se pasa los días poniendo a punto coches de alto rendimiento:\n la marca y el modelo importan menos\n que el sistema de inyección controlado por ordenador\n que los hace volar por el aire.") 

    
    def ocultar_informacion_1():  

        etiqueta2.config(text="")

    Button (ventana, text="ocultar", command=ocultar_informacion_1).grid(column = 4, row=3, padx=5, pady=5)

    
ventana.mainloop()