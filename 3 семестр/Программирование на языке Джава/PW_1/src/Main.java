import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final double ROUBLES_PER_YUAN = 11.91;
        Scanner input = new Scanner(System.in);
        System.out.print("Введите сумму денег в китайских юанях: ");
        int yuan; yuan = input.nextInt();
        System.out.print("Ваша сумма денег в китайских юанях: " + yuan + " китайски");
        if ((yuan % 100) >= 10 && (yuan % 100) < 20) {
            System.out.println("х юаней.");
        }
        else
        {
            int digit = yuan % 10;
            if (digit == 1) {
                System.out.println("й юань.");
            } else if (digit > 1 && digit < 5 ) {
                System.out.println("х юаня.");
            }
            else if (digit >= 5) {
                System.out.println("х юаней.");
            }
        }
        double roubles; roubles = ROUBLES_PER_YUAN * yuan;
        System.out.println("Ваша сумма денег в российских рублях: " + roubles);
    }
}