import java.util.Scanner;

public class TestLoanClass {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Получить годовую процентную ставку
        System.out.print("Введите годовую процентную ставку, например, 8.25: ");
        double annualInterestRate = input.nextDouble();

        // Получить срок кредита в годах
        System.out.print("Введите срок кредита в годах: ");
        int numberOfYears = input.nextInt();

        // Получить сумму кредита
        System.out.print("Введите сумму кредита в руб., например, 120000.95: ");
        double loanAmount =  input.nextDouble();

        // Создать объект типа Loan
        Loan loan = new Loan(annualInterestRate, numberOfYears, loanAmount);

        // Отобразить дату взятия, ежемесячный платеж и общую стоимость кредита
        System.out.println("Дата взятия кредита: " + loan.getLoanDate().toString());
        System.out.println("Ежемесячный платеж по кредиту равен "
                + (int)(loan.getMonthlyPayment() * 100) / 100.0 + " руб.");
        System.out.println("Общая стоимость кредита равна "
                + (int)(loan.getTotalPayment() * 100) / 100.0 + " руб.");
    }
}