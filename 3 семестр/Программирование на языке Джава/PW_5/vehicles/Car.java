package vehicles;

public class Car extends Vehicle
{
    public Car(String model, String license, String color, int year, String ownerName, String insuranceNumber)
    {
        super(model, license, color, year, ownerName, insuranceNumber);
        this.engineType = "Combustion";
    }

    public String vehicleType()
    { return "Car"; }

    public String toString()
    { return "Vehicle Type: " + vehicleType() + super.toString(); }
}
