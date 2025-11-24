data class Order(val orderId: Int, val customerId: Int, val products: List<String>, val totalPrice: Double)

object OrderManager {
    private val orders = mutableListOf<Order>()

    fun addOrder(order: Order) {orders.add(order)}

    fun removeOrdersBelowPrice(threshold: Double) {orders.removeAll {it.totalPrice < threshold}}

    fun getUniqueCustomers(): List<Int> {return orders.map { it.customerId }.distinct()}

    fun getTotalRevenue(): Double {return orders.sumOf { it.totalPrice }}

    fun getTop3MostExpensive(): List<Order> {return orders.sortedByDescending { it.totalPrice }.take(3)}

    fun printAllOrders() {
        println("Все заказы:")
        orders.forEach { println(it) }
    }
}

fun main() {
    OrderManager.apply {
        addOrder(Order(1, 101, listOf("Ноутбук", "Мышь"), 77998.00))
        addOrder(Order(2, 102, listOf("Телефон"), 46999.00))
        addOrder(Order(3, 101, listOf("Клавиатура"), 5999.00))
        addOrder(Order(4, 103, listOf("Монитор", "Коврик"), 27998.00))
        addOrder(Order(5, 104, listOf("Системный блок"), 69999.00))
    }
    OrderManager.printAllOrders()
    println("\nУникальные клиенты: ${OrderManager.getUniqueCustomers()}")
    println("Общий доход: $${OrderManager.getTotalRevenue()}")
    println("Топ-3 заказа: ${OrderManager.getTop3MostExpensive()}")
    OrderManager.removeOrdersBelowPrice(50000.00)
    println("\nПосле удаления заказов дешевле 50000.00:")
    OrderManager.printAllOrders()
}
