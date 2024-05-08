import java.util.Scanner;
public class Eslalon {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String palabraActual = scanner.next();
        int contadorDeBanderi = 0;
        
        while (!palabraActual.equals("META")) {
            contadorDeBanderi = contadorDeBanderi + 1;
            System.out.println(palabraActual + " " + contadorDeBanderi);
            palabraActual = scanner.next();
        }
    }
}
