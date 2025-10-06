package banking

class BankAccount(
    val accountNumber: String,
    private var _balance: Double,
    private var _ownerName: String
) {
    private var transactionCount: Int = 0

    init { require(_balance >= 0) {"Начальный баланс не может быть отрицательным"} }

    constructor(accountNumber: String, ownerName: String):
            this(accountNumber, 0.0, ownerName)

    var balance: Double
        get() = Math.round(_balance * 100) / 100.0
        private set(value) { _balance = value }

    var ownerName: String
        get() = _ownerName
        set(value) {
            require(value.length >= 2) {"Имя владельца должно содержать минимум 2 символа"}
            _ownerName = value
        }

    fun deposit(amount: Double) {
        require(amount > 0) {"Сумма пополнения должна быть положительной"}
        _balance += amount
        logTransaction()
    }

    fun withdraw(amount: Double): Boolean {
        require(amount > 0) {"Сумма снятия должна быть положительной"}
        if (amount <= _balance) {
            _balance -= amount
            logTransaction()
            return true
        }
        return false
    }

    fun getAccountInfo(): String {
        return "Счет: $accountNumber\n" +
                "Владелец: $ownerName\n" +
                "Баланс: $balance\n" +
                "Операций: $transactionCount"
    }

    private fun logTransaction()
    { transactionCount++ }
}