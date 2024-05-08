import java.util.Locale;
import java.util.Scanner;

public class AlturaMinima {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ENGLISH);

        int numChildren = scanner.nextInt();
        float[] heights = new float[numChildren];
        for (int i = 0; i < numChildren; i++) {
            heights[i] = scanner.nextFloat();
        }
        float minHeight = scanner.nextFloat();

        for (int i = 0; i < numChildren ; i++) {
            if (heights[i] >= minHeight) {
                System.out.println("SI");
            } else {
                System.out.println("NO");
            }
        }
    }
}
