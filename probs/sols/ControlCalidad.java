import java.util.Scanner;

public class ControlCalidad {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        boolean chasis = scanner.nextBoolean();
        boolean ruedas = scanner.nextBoolean();
        boolean motor = scanner.nextBoolean();
        boolean electronica = scanner.nextBoolean();
        boolean luces = scanner.nextBoolean();

        System.out.print("El estado del chasis es: ");
        if (chasis) {
            System.out.println("correcto");
        } else {
            System.out.println("defectuoso");
        }
        System.out.print("El estado de las ruedas es: ");
        if (ruedas) {
            System.out.println("correcto");
        } else {
            System.out.println("defectuoso");
        }
        System.out.print("El estado del motor es: ");
        if (motor) {
            System.out.println("correcto");
        } else {
            System.out.println("defectuoso");
        }
        System.out.print("El estado de la electrónica es: ");
        if (electronica) {
            System.out.println("correcto");
        } else {
            System.out.println("defectuoso");
        }
        System.out.print("El estado de las luces es: ");
        if (luces) {
            System.out.println("correcto");
        } else {
            System.out.println("defectuoso");
        }
        System.out.print("El estado general del coche es: ");
        if (chasis && ruedas && motor && electronica && luces) {
            System.out.println("correcto");
        } else {
            System.out.println("defectuoso");
        }
    }
}
