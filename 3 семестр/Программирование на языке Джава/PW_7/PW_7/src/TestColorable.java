public class TestColorable
{
    public static void main(String[] args)
    {
        NewGeometricObject[] objects = new NewGeometricObject[5];
        objects[0] = new Circle(3);
        objects[1] = new Square(5);
        objects[2] = new Rectangle(4, 6);
        objects[3] = new Triangle3(3, 4, 5);
        objects[4] = new Square(7);

        for (NewGeometricObject obj : objects)
        {
            System.out.println(obj);
            System.out.println("Площадь: " + obj.getArea());

            if (obj instanceof Colorable)
            { ((Colorable) obj).howToColor(); }

            System.out.println();
        }
    }
}
