
class Alumno:
    Nombre= None
    Nota= None
    def __init__(self, Nota):
        self.Nombre= ("Alfonzo")
        self.Nota= Nota


Prueba= Alumno (int(input("¿Que nota obtuvo?  " )))
print ("En la prueba",Prueba.Nombre,"Obtuvo: ", Prueba.Nota)
