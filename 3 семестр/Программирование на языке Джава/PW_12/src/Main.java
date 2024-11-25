public class Main
{
    public static void main(String[] args)
    {
        Runnable task = () -> {
            AppSettings settings = AppSettings.getInstance();
            settings.setSetting("тема", Thread.currentThread().getName());
            System.out.println("Поток " + Thread.currentThread().getName() + " установил тему: " + settings.getSetting("тема"));
        };

        Thread thread1 = new Thread(task, "\"Тёмная тема\""); thread1.start();
        Thread thread2 = new Thread(task, "\"Светлая тема\""); thread2.start();

        AppSettings instance1 = AppSettings.getInstance();
        AppSettings instance2 = AppSettings.getInstance();
        System.out.println("Экземпляры одинаковы? " + (instance1 == instance2));
    }
}
