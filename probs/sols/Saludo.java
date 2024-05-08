import java.util.Scanner;

public class Saludo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer el nombre de la persona
        String nombre = scanner.nextLine();

        // Saludar a la persona
        System.out.println("Hola " + nombre + "!");
        
        scanner.close();
    }
}
