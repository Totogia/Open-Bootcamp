public class Auto {
    public static void main(String[] args) {
        auto miauto = new auto();
        miauto.AgregarPuerta();
        System.out.println("Puertas del Auto: " + miauto.puertas);

    }
    static class auto {
        public int puertas = 2;
        public void AgregarPuerta() {
            this.puertas++;
        }
    }
}
