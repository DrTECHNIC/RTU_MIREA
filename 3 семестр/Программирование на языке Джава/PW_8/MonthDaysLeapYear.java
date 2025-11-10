import java.util.InputMismatchException;
import java.util.Scanner;

public class MonthDaysLeapYear
{
    public static void main(String[] args)
    {
        String[] months = {"январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"};
        int[] dom = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        Scanner input = new Scanner(System.in);
        try
        {
            System.out.print("Введите целое число от 1 до 12: ");
            int month = input.nextInt();

            if (month == 2)
            {
                System.out.print("Введите год: ");
                int year = input.nextInt();
                if (isLeapYear(year))
                    dom[1] = 29;
            }
            System.out.println("Месяц: " + months[month - 1] + ", дней: " + dom[month - 1]);
        }
        catch (ArrayIndexOutOfBoundsException e)
        { System.out.println("Недопустимое число"); }
        catch (InputMismatchException e)
        { System.out.println("Введите целое число"); }
    }

    public static boolean isLeapYear(int year)
    { return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0); }
}
