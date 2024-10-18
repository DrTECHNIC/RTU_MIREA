public class Square extends NewGeometricObject implements Colorable
{
    private double side;

    // Безаргументный конструктор
    public Square() { this(0.0); }

    // Конструктор с параметром
    public Square(double side) { this.side = side; }

    // Getter для стороны
    public double getSide() { return side; }

    // Setter для стороны
    public void setSide(double side) { this.side = side; }

    @Override
    public double getArea() { return side * side; }

    public double getPerimeter() { return 4 * side; }

    @Override
    public void howToColor() { System.out.println("Раскрасьте все четыре стороны."); }

    @Override
    public String toString() { return "Квадрат со стороной = " + side; }
}
