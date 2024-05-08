import java.util.Scanner;

public class CartaFormal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer los datos del cliente
        String tratamiento = scanner.nextLine();
        String nombre = scanner.nextLine();
        String apellido1 = scanner.nextLine();
        String apellido2 = scanner.nextLine();

        // Generar y mostrar el encabezado de la carta
        System.out.println(tratamiento + " " + apellido1 + " " + apellido2 + ", " + nombre);
        System.out.println();
	System.out.println("El principal objetivo de la presente carta...");

        scanner.close();

    }


}

