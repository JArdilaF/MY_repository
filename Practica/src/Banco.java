//Encapsulamiento

class Cuenta implements Interfaz{
    private String Titular;
    private double Saldo;

    public Cuenta(String Titular, double Saldo){
        this.Titular = Titular;
        this.Saldo = Saldo;
    }

    public void depositar(double monto){
        Saldo += monto;
        if (monto > 0){
            System.out.println("Su deposito por "+ monto +" fue exitoso, su nuevo saldo es "+ Saldo);
        }else {
            System.out.println("Noo puede ingresar un monto de negativo");
        }
    }

    public void retirar(double retiro){
        if (retiro > Saldo){
            System.out.println("No puedes retirar esta cantidad de dinero, tu Saldo es insuficiente");
        }else {
            Saldo -= retiro;
            System.out.println("Retiro exitoso, Su nuevo saldo es: " + Saldo);
        }
    }

    @Override
    public void imprimir(){
        System.out.println("hollaaaaaaa");
    }
}


public class Banco {
    public static void main(String[] args) {
        Cuenta cuenta = new Cuenta("Yo", 5000);

        cuenta.imprimir();

        cuenta.depositar(500);

        cuenta.retirar(6000);

    }
}
