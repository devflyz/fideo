import java.util.Scanner;
public class JumpJump {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numeroActual = scanner.nextInt();
        int numeroAnterior = numeroActual;
        int saltos = 0;
        while (numeroActual != -1) {
            if (numeroAnterior < numeroActual) {
                saltos++;
            }
            numeroAnterior = numeroActual;
            numeroActual = scanner.nextInt();
        }
        System.out.println(saltos);
    }
}
