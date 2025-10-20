// 10. abstract fun
abstract class BankCard(val cardNumber: String, private val pinCode: Int) { // 9. private val pinCode
    abstract fun getBalance(): Double
    abstract fun updateBalance(amount: Double)

    // 16. проверка пин-кода
    fun verifyPin(pin: Int): Boolean = pin == pinCode
}

class CreditCard(
    cardNumber: String,
    pinCode: Int,
    private val creditLimit: Double // 4. private
) : BankCard(cardNumber, pinCode) {
    private var debt: Double = 0.0

    // 1. было creditLimit + debt
    //   стало creditLimit - debt
    override fun getBalance(): Double = creditLimit - debt

    // 2. исправил логику обновления баланса с учетом типа операции
    override fun updateBalance(amount: Double) {
        // пополнение -> уменьшение долга
        if (amount > 0)
            debt = maxOf(0.0, debt - amount)
        // снятие -> увеличение долга, но не больше лимита
        else
            // 5. проверка кредитного лимита
            if (debt - amount <= creditLimit) debt -= amount
            else throw IllegalArgumentException("Превышен кредитный лимит")
    }

    // 3. убрал ненужный модификатор open
    fun getAvailableCredit(): Double = creditLimit - debt
}

class DebitCard(cardNumber: String, pinCode: Int) : BankCard(cardNumber, pinCode) {
    private var balance: Double = 0.0

    override fun getBalance(): Double = balance

    // 6. было balance = amount
    //   стало balance += amount
    override fun updateBalance(amount: Double) {
        // 7. проверка на отрицательный баланс
        if (amount < 0 && balance < -amount)
            throw IllegalArgumentException("Недостаточно средств")
        balance += amount
    }

    // 8. убрал неиспользуемый класс AdditionalInfo
}

enum class TransactionType {
    WITHDRAWAL, DEPOSIT
}

// 11. вынес функцию fromString за пределы enum класса
fun getTransactionTypeFromString(type: String): TransactionType {
    return when (type.uppercase()) {
        "WITHDRAWAL" -> TransactionType.WITHDRAWAL
        "DEPOSIT" -> TransactionType.DEPOSIT
        else -> throw IllegalArgumentException("Неизвестный тип транзакции: $type")
    }
}

// 13. функция для генерации ID транзакции (вынес отдельно)
private fun generateTransactionId(): String {
    return System.currentTimeMillis().toString() + (0..999).random()
}

data class Transaction(
    val cardNumber: String,
    val amount: Double,
    val date: String,
    val type: TransactionType,
    // 14. инициализация transactionId с помощью отдельной функции
    val transactionId: String = generateTransactionId()
) {
    // 12. убрал избыточные геттер и сеттер
}

class ATM {
    // 15. исправил инициализацию transactions: убрал неправильный конструктор и сразу инициализировал
    private val transactions: MutableList<Transaction> = mutableListOf()

    fun makeTransaction(
        card: BankCard,
        pin: Int,
        amount: Double,
        date: String,
        type: TransactionType
    ): Boolean {
        // 17. проверка пин-кода
        if (!card.verifyPin(pin)) {
            println("Неверный PIN-код")
            return false
        }

        // 18. проверка положительности суммы
        if (amount <= 0) {
            println("Сумма должна быть положительной")
            return false
        }

        return try {
            when (type) {
                TransactionType.WITHDRAWAL -> {
                    // 19. для дебетовой карты проверка выполняется в методе updateBalance
                    card.updateBalance(-amount)
                    // 20. транзакции получают ID через конструктор
                    transactions.add(Transaction(card.cardNumber, amount, date, type))
                    true
                }
                TransactionType.DEPOSIT -> {
                    card.updateBalance(amount)
                    transactions.add(Transaction(card.cardNumber, amount, date, type))
                    true
                }
                // 21. в Kotlin when с enum не требует else, если покрыты все случаи
            }
        } catch (e: IllegalArgumentException) {
            // 28. обработка исключений
            println("Ошибка: ${e.message}")
            false
        }
    }

    fun printTransactions(cardNumber: String) {
        val cardTransactions = transactions.filter { it.cardNumber == cardNumber }
        // проверка на пустой список транзакций
        if (cardTransactions.isEmpty()) {
            println("Нет транзакций по карте $cardNumber")
            return
        }

        println("Транзакции по карте $cardNumber:")
        cardTransactions.forEach {
            // 22. вывод ID транзакции
            println("${it.date} [${it.transactionId}]: ${it.type} ${it.amount}")
        }
    }

    // 23. возврат неизменяемого списка
    fun getAllTransactions(): List<Transaction> = transactions.toList()
}

// функция для преобразования строки в TransactionType
fun stringToTransactionType(type: String): TransactionType {
    return when (type.uppercase()) {
        "WITHDRAWAL" -> TransactionType.WITHDRAWAL
        "DEPOSIT" -> TransactionType.DEPOSIT
        else -> throw IllegalArgumentException("Неизвестный тип транзакции: $type")
    }
}

fun main() {
    val atm = ATM()

    val creditCard = CreditCard("1234-5678-9012-3456", 1234, 10000.0)
    val debitCard = DebitCard("9876-5432-1098-7654", 5678)

    debitCard.updateBalance(5000.0)

    // 24. исправил передачу строки на передачу enum
    val success1 = atm.makeTransaction(creditCard, 1234, 2000.0, "2025-01-15", TransactionType.WITHDRAWAL)
    val success2 = atm.makeTransaction(debitCard, 5678, 1000.0, "2025-01-15", TransactionType.DEPOSIT)

    println("Операция снятия: ${if (success1) "успешно" else "неудачно"}")
    println("Операция пополнения: ${if (success2) "успешно" else "неудачно"}")

    println("Баланс кредитной карты: ${creditCard.getBalance()}")

    println("Доступный кредит: ${creditCard.getAvailableCredit()}")
    println("Баланс дебетовой карты: ${debitCard.getBalance()}")

    atm.printTransactions("1234-5678-9012-3456")
    atm.printTransactions("9876-5432-1098-7654")

    try {
        val transactionType = stringToTransactionType("withdrawal")
        println("Преобразованный тип транзакции: $transactionType")
    } catch (e: IllegalArgumentException) {
        println(e.message)
    }
}
