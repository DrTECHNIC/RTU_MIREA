class GenericStack<E>
{
    private E[] elements;
    private int size;

    @SuppressWarnings("unchecked")
    public GenericStack()
    {
        elements = (E[]) new Object[10];
        size = 0;
    }

    public void push(E item)
    {
        if (size == elements.length)
            resize();
        elements[size++] = item;
    }

    public E pop()
    {
        if (isEmpty())
            throw new IllegalStateException("Стек пуст!");
        return elements[--size];
    }

    public E peek()
    {
        if (isEmpty())
            throw new IllegalStateException("Стек пуст!");
        return elements[size - 1];
    }

    public boolean isEmpty()
    { return size == 0; }

    public int getSize()
    { return size; }

    @SuppressWarnings("unchecked")
    private void resize()
    {
        E[] newArray = (E[]) new Object[elements.length * 2];
        System.arraycopy(elements, 0, newArray, 0, elements.length);
        elements = newArray;
    }

    @Override
    public String toString()
    {
        StringBuilder sb = new StringBuilder("стек: ");
        for (int i = 0; i < size; i++)
            sb.append(elements[i]).append(" ");
        return sb.toString();
    }
}