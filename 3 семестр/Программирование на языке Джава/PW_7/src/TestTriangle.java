import java.util.Scanner;

public class TestTriangle
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.print("Введите сторону 1: ");
        double side1 = input.nextDouble();
        System.out.print("Введите сторону 2: ");
        double side2 = input.nextDouble();
        System.out.print("Введите сторону 3: ");
        double side3 = input.nextDouble();

        System.out.print("Введите цвет: ");
        String color = input.next();
        System.out.print("Треугольник закрашен (true/false)? ");
        boolean isFilled = input.nextBoolean();

        Triangle1 triangle = new Triangle1(side1, side2, side3);
        triangle.setColor(color);
        triangle.setFilled(isFilled);

        System.out.println(triangle.toString());
        System.out.println("Площадь: " + triangle.getArea());
        System.out.println("Периметр: " + triangle.getPerimeter());
        System.out.println("Цвет: " + triangle.getColor());
        System.out.println("Закрашен: " + triangle.isFilled());
    }
}
