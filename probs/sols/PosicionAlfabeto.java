import java.util.Scanner;
public class PosicionAlfabeto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Creamos un array del abecedario

        char[] abecedario = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        
        String paraula = scanner.next();

	// Pasamos las letras a minusculas
	paraula = paraula.toLowerCase();

        for (int i = 0 ; i < paraula.length() ; i++) {
            for (int j = 0 ; j < abecedario.length ; j++) {
                if (paraula.charAt(i) == abecedario[j]) {
                    System.out.println(j);
                }
            }
        }
    }
    
}
