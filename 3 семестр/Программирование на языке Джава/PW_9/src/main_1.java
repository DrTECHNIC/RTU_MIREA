import java.util.ArrayList;
import java.util.Arrays;

public class main_1
{

    // Метод для удаления дубликатов из ArrayList
    public static <T> ArrayList<T> removeDuplicates(ArrayList<T> list)
    {
        ArrayList<T> result = new ArrayList<>();
        for (T element : list)
            if (!result.contains(element))
                result.add(element);
        return result;
    }

    // Метод линейного поиска элемента в массиве
    public static <T> int linearSearch(T[] array, T key)
    {
        for (int i = 0; i < array.length; i++)
            if (array[i].equals(key))
                return i;
        return -1;
    }

    // Метод для поиска наибольшего элемента в массиве
    public static <T extends Comparable<T>> T findMax(T[] array)
    {
        if (array == null || array.length == 0)
            return null;
        T max = array[0];
        for (T element : array)
            if (element.compareTo(max) > 0)
                max = element;
        return max;
    }

    // Метод для поиска наибольшего элемента в двумерном массиве
    public static <T extends Comparable<T>> T findMaxIn2DArray(T[][] array)
    {
        if (array == null || array.length == 0)
            return null;
        T max = array[0][0];
        for (T[] row : array)
            for (T element : row)
                if (element.compareTo(max) > 0)
                    max = element;
        return max;
    }

    // Основная функция программы
    public static void main(String[] args)
    {
        // Пример работы removeDuplicates
        System.out.println();
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 2, 3, 4, 5, 4));
        System.out.println("Исходный список: " + list);
        ArrayList<Integer> uniqueList = removeDuplicates(list);
        System.out.println("Список без дубликатов: " + uniqueList);

        // Пример работы linearSearch
        System.out.println();
        Integer[] array = {10, 20, 30, 40, 50};
        int key = 30;
        int position = linearSearch(array, key);
        System.out.println("Позиция элемента " + key + " в массиве: " + position);
        key = 60;
        position = linearSearch(array, key);
        System.out.println("Позиция элемента " + key + " в массиве: " + position);

        // Пример работы findMax
        System.out.println();
        Circle[] circles = { new Circle(3.5), new Circle(2.1), new Circle(5.4) };
        Circle largestCircle = findMax(circles);
        System.out.println("Наибольший круг: " + largestCircle);

        // Пример работы findMaxIn2DArray
        System.out.println();
        Circle[][] circle2DArray = {
                { new Circle(3.5), new Circle(2.1), new Circle(4.0) },
                { new Circle(5.4), new Circle(1.2), new Circle(3.9) }
        };
        Circle largestCircleIn2D = findMaxIn2DArray(circle2DArray);
        System.out.println("Наибольший круг в двумерном массиве: " + largestCircleIn2D);
    }
}
