import java.util.Scanner;
public class PosicionLetraTexto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String linea = scanner.nextLine();
        String lletraBuscar = scanner.next();
        char lletraChar = lletraBuscar.charAt(0);

        boolean encontrado = false;
        for (int i = 0 ; i < linea.length() ; i++) {
            if (linea.charAt(i) == lletraChar) {
                System.out.println(i);
                encontrado = true;
                break;
            }
        }
        if (encontrado == false) {
            System.out.println(-1);
        }
    }
}
