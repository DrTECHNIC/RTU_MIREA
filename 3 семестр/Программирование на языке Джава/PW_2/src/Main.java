public class Main {
    public static void main(String[] args) {
        Car car_1 = new Car();
        Car car_2 = new Car("LADA Priora", "A123BK", "Black", 2009);
        Car car_3 = new Car("KAMAZ-54901", "White");

        System.out.print("\nИнформация о втором автомобиле: ");
        car_2.To_String();

        System.out.println("\nМодель третьего автомобиля: " + car_3.get_model());
        System.out.println("Номер второго автомобиля: " + car_2.get_license());
        System.out.println("Цвет третьего автомобиля: " + car_3.get_color());
        System.out.println("Год выпуска первого автомобиля: " + car_1.get_model());

        car_1.set_model("Ford Focus");
        car_1.set_license("5PPP064");
        car_1.set_color("Dark Blue");
        car_1.set_year(2018);
        System.out.print("\nОбновленная информация о первом автомобиле: ");
        car_1.To_String();

        int year = 2024;
        System.out.println("\nВозраст первого автомобиля: " + car_1.get_car_age(year) + " лет");
    }
}