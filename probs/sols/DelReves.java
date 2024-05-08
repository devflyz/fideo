import java.util.Scanner;
import java.util.Locale;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ENGLISH);


        int cantidad = scanner.nextInt();
        int[] numeros = new int[cantidad];

        for (int i=0 ; i<cantidad ; i++) {
            numeros[i] = scanner.nextInt();
        }

        while (cantidad != 0) {
            System.out.print(numeros[cantidad-1] + " ");
            cantidad--;
        }

    }
}
