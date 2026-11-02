//Getters & Setters, Encapsulación
class Producto{
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        setPrecio(precio);
        setStock(stock);
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        if(precio <= 0 ){
            System.out.println("Precio invalido.");
        }else {
            this.precio = precio;
        }
    }

    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        if(stock < 0){
            System.out.println("Número de stock inválido.");
        }else {
            this.stock = stock;
        }
    }

    double aplicarDescuento(int porcentaje){
        if(porcentaje < 0){
            System.out.println("Descuento inválido");
        } else if (porcentaje == 0) {
            System.out.println("Descuento nulo");
        }else{
            return precio * ((100.0 - porcentaje) /100.0);
        }
        return precio;
    }
}

class ProductoImportado extends Producto{
    private final double impuestoAduana;


    public ProductoImportado(String nombre, double precio, int stock, double impuestoAduana) {
        super(nombre, precio, stock);
        this.impuestoAduana = impuestoAduana;
    }


    public double getPrecioImpuesto(){
        return getPrecio() * ((100 + impuestoAduana) / 100);
    }

    public double getImpuestoAduana() {
        return impuestoAduana;
    }
}

public class Mio {
    public static void main(String[] args) {
        ProductoImportado pro = new ProductoImportado("Mouse", 40000, 5, 5);

        System.out.println("Producto: " + pro.getNombre());
        System.out.println("Precio: " + pro.getPrecio());
        System.out.println("Precio con descuento: " + pro.aplicarDescuento(0));
        System.out.println("stock: " + pro.getStock());
        System.out.println("Impuesto de la aduana: " + pro.getImpuestoAduana());
        System.out.println("Precio final: " + pro.getPrecioImpuesto());

        System.out.println("//////////////////////////////");
        pro.setPrecio(0);
        pro.setStock(-10);

        System.out.println("//////////////////////////////");

        System.out.println("Producto: " + pro.getNombre());
        System.out.println("Precio: " + pro.getPrecio());
        System.out.println("Precio con descuento: " + pro.aplicarDescuento(50));
        System.out.println("stock: " + pro.getStock());
        System.out.println("Impuesto de la aduana: " + pro.getImpuestoAduana());
        System.out.println("Precio final: " + pro.getPrecioImpuesto());
    }
}
