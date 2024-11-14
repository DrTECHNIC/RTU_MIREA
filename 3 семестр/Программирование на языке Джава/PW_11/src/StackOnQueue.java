import java.util.LinkedList;
import java.util.Queue;

public class StackOnQueue
{
    private Queue<Integer> queue1, queue2;

    public StackOnQueue()
    { queue1 = new LinkedList<>(); queue2 = new LinkedList<>(); }

    // void push(int x) Помещает элемент x на вершину стека.
    public void push(int x)
    {
        queue2.add(x);
        while (!queue1.isEmpty())
            queue2.add(queue1.poll());
        Queue<Integer> temp = queue1;
        queue1 = queue2;
        queue2 = temp;
    }

    // int top() Возвращает элемент на вершине стека.
    public int top()
    {
        if (queue1.isEmpty())
            throw new RuntimeException("Стек пуст");
        return queue1.peek();
    }

    //int pop() Удаляет элемент на вершине стека и возвращает его.
    public int pop()
    {
        if (queue1.isEmpty())
            throw new RuntimeException("Стек пуст");
        return queue1.poll();
    }

    // boolean empty() Возвращает true, если стек пуст, в ином случае false.
    public boolean empty()
    {
        if (queue1.isEmpty())
            return true;
        return false;
    }

    @Override
    public String toString()
    { return queue1.toString(); }
}
