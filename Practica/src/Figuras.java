//Polimorfismo, clase y método abstracto

import java.util.ArrayList;

abstract class Figura implements Interfaz{
    public abstract double area();
}

class Circulo extends Figura{
    private double radio;

    public Circulo(double radio){
        this.radio = radio;
    }

    @Override
    public double area(){
        return  Math.PI * Math.pow(radio,2);
    }

    @Override
    public void imprimir(){
        System.out.println("");
    }
}

class Rectangulo extends Figura {
    private double base;
    private double altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double area() {
        return base * altura;
    }

    @Override
    public void imprimir(){
        System.out.println("");
    }
}


public class Figuras {
    public static void main(String[] args) {
        ArrayList<Figura> miFigura = new ArrayList<>();

        miFigura.add(new Circulo(5));
        miFigura.add(new Rectangulo(2, 6));

        int contador = 1;
        for (Figura f : miFigura) {
            System.out.printf("Área de la figura %d: %.2f%n", contador, f.area());
            contador++;
        }
    }
}