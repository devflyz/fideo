import java.util.Scanner;
public class RobotAspiradora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String palabraActual = scanner.next();
        int contadorDeCLEAN = 0;
        
        while (!palabraActual.equals("OBSTACULO")) {
            // contadorDeCLEAN++;
            contadorDeCLEAN = contadorDeCLEAN + 1;
            palabraActual = scanner.next();
        }
        
        System.out.println(contadorDeCLEAN);
    }
}

