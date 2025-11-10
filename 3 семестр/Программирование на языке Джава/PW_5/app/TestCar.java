package app;

import vehicles.Vehicle;
import vehicles.Car;
import vehicles.ElectricCar;

public class TestCar
{
    public static void main(String[] args)
    {
        Vehicle myCar = new Car("Toyota Camry", "ABC123", "Black", 2020, "Daniil", "INS123456");
        Vehicle myElectricCar = new ElectricCar("Tesla Model 3", "XYZ789", "White", 2022, "Alexei", "INS654321", 75);

        myCar.setYear(2021);
        myCar.setOwnerName("Timofei");

        myElectricCar.setInsuranceNumber("INS271105");

        System.out.println("\nBatter Capacity: " + ((ElectricCar) myElectricCar).getBatteryCapacity() + " kWh\n");

        System.out.println(myCar.toString() + "\n\n" + myElectricCar.toString());
    }
}
