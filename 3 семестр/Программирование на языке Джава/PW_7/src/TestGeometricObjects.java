public class TestGeometricObjects {
    public static void main(String[] args) {
        // Треугольник
        Triangle3 triangle = new Triangle3(3, 4, 5);
        triangle.setColor("blue");
        triangle.setFilled(true);

        System.out.println(triangle);
        System.out.println("Площадь: " + triangle.getArea());
        System.out.println("Периметр: " + triangle.getPerimeter());
        System.out.println("Цвет: " + triangle.getColor());
        System.out.println("Закрашен: " + triangle.isFilled());

        // Сравнение кругов
        ComparableCircle circle1 = new ComparableCircle(5);
        ComparableCircle circle2 = new ComparableCircle(7);
        System.out.println("\nБольше круг: " + (circle1.compareTo(circle2) > 0 ? "circle1" : "circle2"));

        // Сравнение с методом max
        Rectangle rectangle1 = new Rectangle(4, 5);
        Rectangle rectangle2 = new Rectangle(3, 6);

        System.out.println("\nНаибольший прямоугольник: " + NewGeometricObject.max(rectangle1, rectangle2));
        System.out.println("\nНаибольший круг: " + NewGeometricObject.max(circle1, circle2));
    }
}
