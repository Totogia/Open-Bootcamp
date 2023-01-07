class Veiculo:
    Color= ("Rojo")
    Ruedas= 4
    Puertas = 3

class coche(Veiculo):
 velocidadMAX= 150
 cilindrada= 1.5



c=coche ()
print ("Caracteristicas de coche") 
print ("color: ",coche.Color)
print ("Ruedas: ", coche.Ruedas)
print ("Puertas: ", coche.Puertas) 
print ("Velocidad Maxima: ", coche.velocidadMAX)
print ("cilindrada: ", coche.cilindrada)
