import java.util.Scanner;
public class LineaDePuntos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cantidad = scanner.nextInt();
        for (int i=0 ; i < cantidad ; i++) {
            System.out.print(".");
        }
    }
}
