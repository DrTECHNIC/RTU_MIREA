class Circle implements Comparable<Circle>
{
    private double radius;

    public Circle(double radius)
    { this.radius = radius; }

    public double getRadius()
    { return radius; }

    @Override
    public int compareTo(Circle other)
    { return Double.compare(this.radius, other.radius); }

    @Override
    public String toString()
    { return "Круг с радиусом " + radius; }
}