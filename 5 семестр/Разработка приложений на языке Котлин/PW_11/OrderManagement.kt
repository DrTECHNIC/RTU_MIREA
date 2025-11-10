data class Product(val id: Int, val name: String, val price: Double)

class Order {
    var products: MutableList<Product> = mutableListOf()
    var totalPrice: Double = 0.0
    var status: String = "PENDING"
    fun calculateTotal() {totalPrice = products.sumOf{it.price}}
}

fun main() {
    val order = Order().apply {
        products.addAll(listOf(
            Product(1, "Laptop", 99999.99),
            Product(2, "Mouse", 6999.99)
        ))
        calculateTotal()
    }

    order.let {
        println("Order total: ${it.totalPrice}")
        it.status = "PROCESSING"
    }

    val discount = order.run {
        val discount = if (totalPrice > 10000) totalPrice * 0.1 else 0.0
        println("Applied discount: $discount")
        totalPrice - discount
    }
    println("Final price: $discount")

    order.apply {
        status = "COMPLETED"
    }.also {
        println("Order status: ${it.status}")
    }
}
