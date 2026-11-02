package Mypackage1;

public class perroCallejero implements Perro{
    boolean ladrar = false;
    String saludo = "";

    @Override
    public void ladrar(boolean ladra) {
        ladrar = ladra;
    }

    @Override
    public void saludar(String saludoPerro){
        saludo = saludo + saludoPerro;
    }

    public void mostrar(){
        System.out.println("El perro ladra?: "+ ladrar);
        System.out.print("El perro te saluda y dice: "+ saludo);
    }
}