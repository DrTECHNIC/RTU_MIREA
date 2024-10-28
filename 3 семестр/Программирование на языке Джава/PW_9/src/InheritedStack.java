import java.util.ArrayList;

class InheritedStack<E> extends ArrayList<E>
{
    public void push(E item)
    { this.add(item); }

    public E pop()
    {
        if (this.isEmpty())
            throw new IllegalStateException("Стек пуст!");
        return this.remove(this.size() - 1);
    }

    public E peek()
    {
        if (this.isEmpty())
            throw new IllegalStateException("Стек пуст!");
        return this.get(this.size() - 1);
    }
}
