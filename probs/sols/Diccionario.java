import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String palabraActual = scanner.next();
        System.out.println("class Dictionari {");
        System.out.println("    String[] words = {");
        
        while (!palabraActual.equals("__END__")) {
            System.out.print("        \""+palabraActual+"\"");
            palabraActual = scanner.next();
            if (!palabraActual.equals("__END__")) {
                System.out.println(",");
            } else {
                System.out.println();
            }
        }
        System.out.println("    };");
        System.out.println("}");

    }
}
