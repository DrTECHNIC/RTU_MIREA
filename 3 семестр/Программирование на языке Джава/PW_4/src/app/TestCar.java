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

        myCar.setColor("Red");
        myElectricCar.setOwnerName("Maxim");

        System.out.println();
        System.out.println(myCar.toString());
        System.out.println();
        System.out.print(myElectricCar.toString());
    }
}
