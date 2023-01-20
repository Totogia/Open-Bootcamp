from logging import root
import tkinter
from tkinter import Button, ttk

window = tkinter.Tk()

window.columnconfigure (0, weight=1)
window.columnconfigure (1, weight=7)

saber = tkinter.StringVar ()

Texto1 =ttk.Label (window, text= "¿A que nivel?" ) 
Texto1.grid (column = 0, row=3, padx=5, pady=5)


r1 = ttk.Radiobutton (window, text= "avanzado", value= "3", variable = saber)
r2 = ttk.Radiobutton (window, text= "intermedio", value= "2", variable = saber)
r3 = ttk.Radiobutton (window, text= "principiante", value= "1", variable = saber)


r1.grid (column = 0, row=4, padx=5, pady=5)
r2.grid (column = 0, row=5, padx=5, pady=5)
r3.grid (column = 0, row=6, padx=5, pady=5)

Texto1 =ttk.Label (window, text= "¿Que programa saber usar mas?" ) 
Texto1.grid (column = 0, row=0, padx=5, pady=5)

programa = tkinter.StringVar ()

Texto1 =ttk.Label (window, text= "¿Que programa saber usar mas?" ) 
Texto1.grid (column = 0, row=0, padx=5, pady=5)

Py = ttk.Radiobutton (window, text= "Python", value= "1", variable = programa)
Java = ttk.Radiobutton (window, text= "Java", value= "2", variable = programa)


Java.grid (column = 0, row=2, padx=5, pady=5)
Py.grid (column = 0, row=1, padx=5, pady=5)


def reset():
    print("Reiniciando...")
    saber.set(None)
    programa.set (None)

boton_reiniciar = Button(window, text ='Reiniciar', command = reset) 
boton_reiniciar.grid (column = 0, row=7, padx=6, pady=5)
window.mainloop ()