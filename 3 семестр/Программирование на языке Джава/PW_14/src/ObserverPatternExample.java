import java.util.ArrayList;
import java.util.List;

// Интерфейс Observer
interface Observer { void update(String message); }

// Класс Subject для управления подписчиками
class Subject
{
    private final List<Observer> observers = new ArrayList<>();
    public void addObserver(Observer observer) { observers.add(observer); }
    public void removeObserver(Observer observer) { observers.remove(observer); }
    public void notifyObservers(String message) { for (Observer observer : observers) { observer.update(message); } }
}

// Класс User, реализующий интерфейс Observer
class User implements Observer
{
    private final String name;
    public User(String name) { this.name = name; }
    @Override public void update(String message) { System.out.println(name + " получил уведомление: " + message); }
}

// Тестовая программа
public class ObserverPatternExample
{
    public static void main(String[] args)
    {
        Subject subject = new Subject();
        User user1 = new User("Андрей");
        User user2 = new User("Даниил");
        User user3 = new User("Сергей");
        subject.addObserver(user1);
        subject.addObserver(user2);
        subject.addObserver(user3);
        System.out.println("Событие: Обновление состояния.");
        subject.notifyObservers("Состояние объекта изменено!");
        subject.removeObserver(user2);
        System.out.println("Событие: Другое обновление.");
        subject.notifyObservers("Новое событие произошло!");
    }
}
