import java.util.ArrayList;

public class MyStack implements Cloneable
{
    private ArrayList<Object> list = new ArrayList<>();

    public boolean isEmpty()
    { return list.isEmpty(); }

    public int getSize()
    { return list.size(); }

    public Object peek()
    { return list.get(list.size() - 1); }

    public Object pop()
    { return list.remove(list.size() - 1); }

    public void push(Object o)
    { list.add(o); }

    @Override
    public String toString()
    { return "MyStack: " + list.toString(); }

    @Override
    public Object clone()
    {
        try
        {
            MyStack myStackClone = (MyStack) super.clone();
            myStackClone.list = new ArrayList<>(this.list);
            return myStackClone;
        }
        catch (CloneNotSupportedException ex)
        { return null; }
    }
}