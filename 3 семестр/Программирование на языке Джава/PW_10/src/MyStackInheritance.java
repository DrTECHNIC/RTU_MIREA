import java.util.ArrayList;

public class MyStackInheritance extends ArrayList<Object>
{
    public boolean isEmpty()
    { return super.isEmpty(); }

    public int getSize()
    { return super.size(); }

    public Object peek()
    { return super.get(super.size() - 1); }

    public Object pop()
    { return super.remove(super.size() - 1); }

    public void push(Object o)
    { super.add(o); }

    @Override
    public String toString()
    { return "MyStackInheritance: " + super.toString(); }
}