import java.util.Scanner;

public class LucesApagadas {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// Creamos un boolean
		boolean resultadoFinal;

		boolean primer = scanner.nextBoolean();
		boolean segundo = scanner.nextBoolean();
		boolean tercero = scanner.nextBoolean();
		boolean cuarto = scanner.nextBoolean();

        // Si una es falsa (cualquiera de las 4), pues resultadoFinal será falso.
		resultadoFinal = primer && segundo && tercero && cuarto;

		System.out.println(resultadoFinal);
	}
} 
