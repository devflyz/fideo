import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);       
        sc.useLocale(Locale.ENGLISH);
        String palabra = sc.next();
        int num = 0;
        while (!palabra.equals("END")){
            num++;
            palabra = sc.next();
        }
        System.out.println(num);
    }
}
