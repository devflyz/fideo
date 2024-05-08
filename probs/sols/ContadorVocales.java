import java.util.Scanner;

public class ContarVocales {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Leemos la frase
        String frase = scanner.nextLine();
        // Creamos un contador
        int contador = 0;

        // Pasamos todas las letras de la frase a minuscula
        frase = frase.toLowerCase();

        for (int i = 0 ; i < frase.length() ; i++) {
            if (frase.charAt(i) == 'a' || frase.charAt(i) == 'e' || frase.charAt(i) == 'i' || frase.charAt(i) == 'o' || frase.charAt(i) == 'u') {
                contador++;
            }
        }
        System.out.println(contador);
    }
}
