import java.util.HashMap;


interface Shape { void draw(); }


class Circle implements Shape
{
    private String color;
    private int x, y, radius;

    public Circle(String color)
    { this.color = color; }

    public void setPosition(int x, int y, int radius)
    { this.x = x; this.y = y; this.radius = radius; }

    public void draw()
    { System.out.printf
            ("""
            Круг:
               цвет    :  %s;
               x       :  %d;
               y       :  %d;
               радиус  :  %d.
            """,
    color, x, y, radius); }


}


class ShapeFactory
{
    private static final HashMap<String, Shape> circleMap = new HashMap<>();

    public static Shape getCircle(String color)
    {
        Circle circle = (Circle) circleMap.get(color);
        if (circle == null)
        {
            circle = new Circle(color);
            circleMap.put(color, circle);
            System.out.println("Создание круга с цветом: " + color);
        }
        return circle;
    }
}


public class FlyweightPatternDemo
{
    private static final String[] colors = {"красный", "зелёный", "синий", "белый", "чёрный", "жёлтый", "оранжевый",
            "фиолетовый", "розовый", "серый", "коричневый", "голубой", "пурпурный", "лавандовый", "бордовый"};

    public static void main(String[] args)
    {
        for (int i = 0; i < 10; i++)
        {
            Circle circle = (Circle) ShapeFactory.getCircle(getRandomColor());
            circle.setPosition(getRandomX(), getRandomY(), 100);
            circle.draw();
        }
    }

    private static String getRandomColor()
    { return colors[(int) (Math.random() * colors.length)]; }

    private static int getRandomX()
    { return (int) (Math.random() * 100); }

    private static int getRandomY()
    { return (int) (Math.random() * 100); }
}
