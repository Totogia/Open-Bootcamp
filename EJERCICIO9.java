package Bootcamp.ejercicio9;

public class EJERCICIO9 {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        Cliente.credito =150;
        Cliente.edad=18;
        Cliente.Nombre=("Fulanito");
        Cliente.telefono=("+xx x xxxx xxxxxx");
        System.out.println("Nombre del cliente: " + Cliente.Nombre);
        System.out.println("Edad del cliente: " + Cliente.edad);
        System.out.println("Telefono del cliente: " + Cliente.telefono);
        System.out.println("Credito del cliente: $" + Cliente.credito);
        System.out.println("-------------------------------------------");
        //////////////////////////////////////////////////////////////////////////////
        Trabajador trabajador = new Trabajador();
        Trabajador.edad=21;
        Trabajador.Nombre=("Pepito");
        Trabajador.telefono=("+yy y yyyy yyyyyy");
        Trabajador.salario=1250;
        System.out.println("Nombre del Trabajador: " + Trabajador.Nombre);
        System.out.println("Edad del Trabajador: " + Trabajador.edad);
        System.out.println("Telefono del Trabajador: " + Trabajador.telefono);
        System.out.println("Salario del Trabajador: $" + Trabajador.salario);
        System.out.println("-------------------------------------------");
    }



}
class Persona {
    static int edad;
    static String telefono;
    static String Nombre;
}
class Cliente extends Persona{
    static int credito;
}
class Trabajador extends Persona {
    static int salario;
}