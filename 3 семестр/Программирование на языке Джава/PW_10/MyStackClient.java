import java.util.Scanner;

public class MyStackClient
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        MyStack stack = new MyStack();

        System.out.println("Введите 5 строк:");
        for (int i = 0; i < 5; i++)
        { stack.push(input.nextLine()); }

        System.out.println("Строки в обратном порядке:");
        while (!stack.isEmpty())
        { System.out.println(stack.pop()); }
    }
}