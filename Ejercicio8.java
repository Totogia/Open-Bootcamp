public class Ejercicio8 {
    public static void main(String[] args) {
       Persona edad = new Persona();
       Persona nombre = new Persona();
        Persona telefono = new Persona();
       edad.setEdad("Edad: " + "18");
       nombre.setNombre("Nombre: " + "Fulanito");
       telefono.setTelefono("Telefono: " + "+XX X XXXX-XXXXXX");
       System.out.println(nombre.getNombre());
        System.out.println(edad.getEdad());
        System.out.println(telefono.getTelefono());


    }

}
class Persona {
    private String edad;
    private String nombre;
    private String telefono;

    public void setEdad(String edad) {
        this.edad = edad;
    }
    public String getEdad() {
        return this.edad;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return this.nombre;
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public String getTelefono() {
        return this.telefono;
    }
}
