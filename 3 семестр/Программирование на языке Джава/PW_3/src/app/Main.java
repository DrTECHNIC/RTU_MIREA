package app;

import vehicles.Car;
import vehicles.ElectricCar;

public class Main
{
    public static void main(String[] args)
    {
        Car myCar = new Car("Daniil", "123ABC");
        myCar.setEngineType("Gasoline");
        System.out.println("Car Owner: " + myCar.getOwnerName());
        System.out.println("Car Insurance Number: " + myCar.getInsuranceNumber());
        System.out.println("Car Engine Type: " + myCar.getEngineType());

        ElectricCar myElectricCar = new ElectricCar("Alexei", "789XYZ", 85);
        System.out.println("\nElectric Car Owner: " + myElectricCar.getOwnerName());
        System.out.println("Electric Car Insurance Number: " + myElectricCar.getInsuranceNumber());
        System.out.println("Electric Car Engine Type: " + myElectricCar.getEngineType());
        System.out.print("Electric Car Battery Capacity: " + myElectricCar.getBatteryCapacity() + " kWh");
    }
}