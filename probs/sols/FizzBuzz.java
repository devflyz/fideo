import java.util.Scanner;
import java.util.Locale;
public class FizzBuzz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ENGLISH);
        int primerValor = scanner.nextInt();
        for (int segundoValor = scanner.nextInt(); primerValor>=segundoValor ; primerValor-- ) {
            if ((primerValor%5==0) && (primerValor%3==0)) {
                System.out.println("FizzBuzz");
            } else if (primerValor%5==0) {
                System.out.println("Buzz");
            } else if (primerValor%3==0) {
                System.out.println("Fizz");
            } else {
                System.out.println(primerValor);
            }
        }
    }
}
