import java.util.Scanner;

public class ReverseString {
        public static void main(String[] args)
        {
                Scanner scanner = new Scanner(System.in);
                String line = scanner.nextLine();

                String[] array = new String[line.length()];

                for (int i = 0 ; i < line.length() ; i++) {
                        array[i] = String.valueOf(line.charAt(line.length() - 1 -i));
                }

                for (int i = 0 ; i < line.length() ; i++) {
                        System.out.print(array[i]);
                }
        }
}
