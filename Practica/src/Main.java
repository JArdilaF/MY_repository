// muestro clases, objetos, atributos, metodos, constructores, herencia, encapsulamiento,

class Bici {
    int cadencia;
    int velocidad;
    int marcha;

    // Se ejecuta al hacer 'new Bici(...)' e inicializa sus atributos
    public Bici(int cadencia, int velocidad, int marcha) {
        this.cadencia = cadencia;
        this.velocidad = velocidad;
        this.marcha = marcha;
    }

    void CambioCadencia(int nueva_cadencia) {
        cadencia = nueva_cadencia;
    }

    void CambioVelocidad(int nueva_velocidad) {
        velocidad = nueva_velocidad;
    }

    void CambioMarcha(int nueva_marcha) {
        marcha = nueva_marcha;
    }

    void mostrar() {
        System.out.print("Cadencia: " + cadencia + ", Velocidad: " + velocidad + ", Marcha: " + marcha);
    }
}

class biciÑera extends Bici {
    boolean pedales;

    // Recibe los datos del padre + su propio dato ('pedales')
    public biciÑera(int cadencia, int velocidad, int marcha, boolean pedales) {
        super(cadencia, velocidad, marcha); // <- Envía los datos al constructor de Bici
        this.pedales = pedales;             // <- Inicializa su propio atributo
    }

    @Override
    void mostrar() {
        super.mostrar(); // Llama al mostrar() de Bici para ver velocidad, marcha, etc.
        System.out.println(", Pedales de aluminio/neocromados: " + pedales);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Bici 1: normal");
        Bici cicla1 = new Bici(45, 15, 3);
        cicla1.mostrar();
        System.out.println(); // Salto de línea

        System.out.println("Bici 2: normal");
        Bici cicla2 = new Bici(60, 5, 1);
        cicla2.mostrar();
        System.out.println();

        System.out.println("Bici 3: Ñera");
        // Pasamos cadencia, velocidad, marcha y el estado de los pedales
        Bici cicla3 = new biciÑera(0, 80, 1, true);
        cicla3.mostrar();
    }
}
