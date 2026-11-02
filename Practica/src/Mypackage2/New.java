package Mypackage2;

import Mypackage1.*;

public class New {
    public static void main(String[] args) {
        perroCallejero perro1 = new perroCallejero();

        perro1.ladrar(true);
        perro1.saludar("Hola Humano");
        perro1.mostrar();
    }
}
