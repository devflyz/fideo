import java.util.Scanner;

public class ClaveAcceso {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int cantidadDeNombres = scanner.nextInt(); // cantidad de numeros de la contraseña

        int[] claveApertura = new int[cantidadDeNombres]; // esta es la clave
        boolean[] estaElNumero = new boolean[cantidadDeNombres];

        for (int i = 0 ; i < cantidadDeNombres ; i++ ) {
            claveApertura[i] = scanner.nextInt();
        }

        int cantidadDeNombresQueConteElSistemaDapertura = scanner.nextInt();

        int[] numerosQueHaPuestoElUsuario = new int[cantidadDeNombresQueConteElSistemaDapertura];

        for (int i = 0 ; i < cantidadDeNombresQueConteElSistemaDapertura ; i++ ) {
            numerosQueHaPuestoElUsuario[i] = scanner.nextInt();
        }

        for (int i = 0 ; i < cantidadDeNombres ; i++) {
            for (int j = 0 ; j < cantidadDeNombresQueConteElSistemaDapertura ; j++) {
                if (claveApertura[i] == numerosQueHaPuestoElUsuario[j]) {
                    estaElNumero[i] = true;
                }
            }
        }

        boolean verificadorFinal = true;

        for (int i =  0 ; i < cantidadDeNombres ; i++) {
            verificadorFinal&=estaElNumero[i];
        }

        if (verificadorFinal) {
            System.out.println("OK");
        } else {
            System.out.println("ERROR");
        }

    }
}
