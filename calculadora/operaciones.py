class Calculadora:
    Numero1= input("Digame el primer numero:")
    Numero2= input("Digame el segundo numero:")
    int_Numero1 = int (Numero1)
    int_Numero2= int (Numero2)
    def suma (int_Numero1, int_Numero2):
        
     return int_Numero1 + int_Numero2

    def resta(int_Numero1, int_Numero2):
        
     return int_Numero1 - int_Numero2
    
    def multiplicar(int_Numero1, int_Numero2):
        
     return int_Numero1 * int_Numero2

    def divide(int_Numero1, int_Numero2):
        
     return int_Numero1 / int_Numero2
    
    
    
    
    print ("Resultado: ",suma(int_Numero1, int_Numero2))
    print ("Resultado: ",resta(int_Numero1, int_Numero2))
    print ("Resultado: ",multiplicar(int_Numero1, int_Numero2))
    print ("Resultado: ",divide(int_Numero1, int_Numero2))

