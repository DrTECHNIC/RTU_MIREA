public class TestTriangleWithException
{
    public static void main(String[] args)
    {
        try
        { Triangle2 triangle = new Triangle2(1, 2, 3); }
        catch (IllegalTriangleException ex)
        { System.out.println("Ошибка: " + ex.getMessage()); }
    }
}
