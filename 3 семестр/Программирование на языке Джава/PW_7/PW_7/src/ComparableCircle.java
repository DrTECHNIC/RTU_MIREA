public class ComparableCircle extends Circle
{
    public ComparableCircle(double radius)
    { super(radius); }

    public int compareTo(ComparableCircle o)
    { return Double.compare(this.getArea(), o.getArea()); }
}
