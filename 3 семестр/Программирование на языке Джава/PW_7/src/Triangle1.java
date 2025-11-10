public class Triangle1 extends GeometricObject
{
    private double side1;
    private double side2;
    private double side3;

    // Конструктор по умолчанию
    public Triangle1()
    { side1 = 1.0; side2 = 1.0; side3 = 1.0; }

    // Конструктор с заданными сторонами
    public Triangle1(double side1, double side2, double side3)
    {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    // Геттеры для сторон
    public double getSide1() { return side1; }
    public double getSide2() { return side2; }
    public double getSide3() { return side3; }

    // Метод для вычисления площади
    public double getArea()
    {
        double s = getPerimeter() / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    // Метод для вычисления периметра
    public double getPerimeter()
    { return side1 + side2 + side3; }

    // Метод toString для описания треугольника
    @Override
    public String toString()
    { return "Треугольник: сторона1 = " + side1 + " сторона2 = " + side2 + " сторона3 = " + side3; }
}
