import java.util.Scanner;
public class CalculadoraFactorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero = scanner.nextInt();

        int resultado = 1;
        while (numero != 0) {
            resultado = resultado * numero;
            numero--;
        }
        System.out.println(resultado);
    }
}
