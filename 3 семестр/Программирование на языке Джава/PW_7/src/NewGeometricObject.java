public abstract class NewGeometricObject implements Comparable<NewGeometricObject>
{
    private String color = "white";
    private boolean filled;
    private java.util.Date dateCreated;

    public NewGeometricObject()
    { dateCreated = new java.util.Date(); }

    public NewGeometricObject(String color, boolean filled)
    {
        dateCreated = new java.util.Date();
        this.color = color;
        this.filled = filled;
    }

    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }
    public boolean isFilled() { return filled; }
    public void setFilled(boolean filled) { this.filled = filled; }
    public java.util.Date getDateCreated() { return dateCreated; }

    @Override
    public String toString()
    { return "создан " + dateCreated + ", цвет: " + color + ", заливка: " + filled; }

    // Сравнение по площади
    @Override
    public int compareTo(NewGeometricObject o)
    { return Double.compare(this.getArea(), o.getArea()); }

    // Абстрактный метод для получения площади
    public abstract double getArea();

    // Статический метод для поиска наибольшего объекта
    public static NewGeometricObject max(NewGeometricObject o1, NewGeometricObject o2)
    { return (o1.compareTo(o2) >= 0) ? o1 : o2; }
}
