import java.util.Scanner;

public class MenjarRestaurant {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("MENÚ:");
        System.out.println("1.- DESAYUNOS");
        System.out.println("2.- ALMUERZOS");
        System.out.println("3.- MERIENDAS");
        System.out.println("4.- CENAS");
        
        int opcion = scanner.nextInt();

        int A = scanner.nextInt();
        int B = scanner.nextInt();

        String comida = "";
        if (opcion == 1) {
            comida = "DESAYUNOS";
        } else if (opcion == 2) {
            comida = "ALMUERZOS";
        } else if (opcion == 3) {
            comida = "MERIENDAS";
        } else if (opcion == 4) {
            comida = "CENAS";
        } else {
            System.out.println("OPCIÓN INEXISTENTE !!");
            return;
        }

        System.out.println("Total " + comida + " del restaurante A y B: " + (A+B));
    }
}
