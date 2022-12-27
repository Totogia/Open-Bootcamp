public class Auto {
    public static void main(String[] args) {
        Auto miauto= new Auto();
        miauto.AgregarPuerta();
        System.out.println("Puertas del Auto: " + miauto.puertas);

    }
    static class Auto {
        public int puertas = 2;
        public void AgregarPuerta() {
             this.puertas++;
        }
    }
}