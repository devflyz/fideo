import java.util.Scanner;
public class SumaDigitos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String numero = scanner.next();
        int suma = 0;
        for (int i = 0 ; i < numero.length() ; i++) {
            char numeroEnChar = numero.charAt(i);
            // Vale ahora mismo ese numero en char lo tenemos que pasar a INT
            // PARA PASARLO A INT, LO PASAREMOS A STRING Y LUEGO A INT.
            // DE CHAR A STRING, Y LUEGO DE STRING A INT

            // String.valueOf(elNombreDelChar) --> ESTO LO PASA A STRING
            // Integer.parseInt(variableTipoString) --> ESTO LO PASA A INT
            int numeroEnInt = Integer.parseInt(String.valueOf(numeroEnChar));
            // Lo sumo al valor que tenemos.
            suma+=numeroEnInt;
        }
        System.out.println(suma);
    }
}