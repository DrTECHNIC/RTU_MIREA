import java.util.Scanner;

public class main_2
{
    public static void main(String[] args)
    {
        // Пример использования GenericStack с массивом
        GenericStack<String> stack = new GenericStack<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите 5 строк для стека:");
        for (int i = 0; i < 5; i++)
        {
            String input = scanner.nextLine();
            stack.push(input);
        }

        System.out.println("Стек (в прямом порядке): " + stack);
        System.out.println("Стек (в обратном порядке): ");
        while (!stack.isEmpty())
            System.out.println(stack.pop());

        // Пример использования InheritedStack
        InheritedStack<String> inheritedStack = new InheritedStack<>();

        System.out.println("\nВведите 5 строк для наследуемого стека:");
        for (int i = 0; i < 5; i++)
        {
            String input = scanner.nextLine();
            inheritedStack.push(input);
        }

        System.out.println("Наследуемый стек (в прямом порядке): " + inheritedStack);
        System.out.println("Наследуемый стек (в обратном порядке): ");
        while (!inheritedStack.isEmpty())
            System.out.println(inheritedStack.pop());

        scanner.close();
    }
}
