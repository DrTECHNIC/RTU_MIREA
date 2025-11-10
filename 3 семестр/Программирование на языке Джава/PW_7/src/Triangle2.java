public class Triangle2 extends GeometricObject {
    private double side1;
    private double side2;
    private double side3;

    public Triangle2()
    { side1=1.0; side2=1.0; side3=1.0; }

    // Конструктор с проверкой сторон
    public Triangle2(double side1, double side2, double side3) throws IllegalTriangleException
    {
        if (side1 + side2 <= side3 || side1 + side3 <= side2 || side2 + side3 <= side1)
        { throw new IllegalTriangleException("Стороны треугольника не удовлетворяют правилу треугольника."); }
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public double getSide1() { return side1; }
    public double getSide2() { return side2; }
    public double getSide3() { return side3; }

    public double getArea()
    {
        double s = getPerimeter() / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    public double getPerimeter()
    { return side1 + side2 + side3; }

    @Override
    public String toString()
    { return "Треугольник: сторона1 = " + side1 + " сторона2 = " + side2 + " сторона3 = " + side3; }
}
