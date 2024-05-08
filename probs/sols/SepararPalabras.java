import java.util.Scanner;

public class SepararPalabras {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer las cinco palabras
        String palabra1 = scanner.next();
        String palabra2 = scanner.next();
        String palabra3 = scanner.next();
        String palabra4 = scanner.next();
        String palabra5 = scanner.next();

        // Imprimir cada palabra en una nueva línea
        System.out.println(palabra1);
        System.out.println(palabra2);
        System.out.println(palabra3);
        System.out.println(palabra4);
        System.out.println(palabra5);

        scanner.close();
    }
}
