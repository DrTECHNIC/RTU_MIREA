public class StackOnQueueTest
{
    public static void main(String[] args)
    {
        StackOnQueue stack = new StackOnQueue();
        stack.push(1); stack.push(2);
        System.out.println("Объект, находящийся на вершине стека (без удаления): " + stack.top());
        System.out.println("объект, находящийся на вершине стека (с удалением): " + stack.pop());
        System.out.println("Проверка стека на пустоту:  " + stack.empty());
        System.out.println("Информация о всех элементах стека: " + stack.toString());
    }
}
