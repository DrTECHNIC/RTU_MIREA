import java.util.ArrayList;

public class List<T>
{
    private ArrayList<T> elements;

    public List()
    { elements = new ArrayList<>(); }

    public void add(T element)
    { elements.add(element); }

    public T get(int index)
    { return elements.get(index); }

    public void remove(int index)
    { elements.remove(index); }

    public int size()
    { return elements.size(); }

    public boolean contains(T element)
    { return elements.contains(element); }

    @Override
    public String toString()
    { return elements.toString(); }
}
