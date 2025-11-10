public class Car
{
    private String model;
    private String license;
    private String color;
    private int year;
    
    public Car(String model, String license, String color, int year)
    {
        this.model = model;
        this.license = license;
        this.color = color;
        this.year = year;
    }
    public Car()
    {
        this.model = "Неизвестно";
        this.license = "Неизвестно";
        this.color = "Неизвестно";
        this.year = -1;
    }
    public Car(String model, String color)
    {
        this.model = model;
        this.license = "Неизвестно";
        this.color = color;
        this.year = -1;
    }

    public void To_String()
    { System.out.println(model + " " + license + " " + color + " " + year); }

    public String get_model() { return model; }
    public String get_license() { return license; }
    public String get_color() { return color; }
    public int get_year() { return year; }

    public void set_model(String model) { this.model = model; }
    public void set_license(String license) { this.license = license; }
    public void set_color(String color) { this.color = color; }
    public void set_year(int year) { this.year = year; }

    public int get_car_age(int year) { return (year - this.year); }
}
