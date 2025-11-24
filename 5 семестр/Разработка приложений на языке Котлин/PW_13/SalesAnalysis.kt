data class Sale(val date: String, val product: String, val quantity: Int, val pricePerUnit: Double)

class SalesAnalyzer(private val sales: List<Sale>) {

    fun getTotalRevenue(): Double {return sales.sumOf {it.quantity * it.pricePerUnit}}

    fun getSalesByProduct(): Map<String, Int> {return sales.groupBy {it.product}.mapValues {(_, sales) -> sales.sumOf {it.quantity}}}

    fun getSalesByMonth(month: String): List<Sale> {return sales.filter { it.date.split("-")[1] == month }}

    fun getTopProductByRevenue(): String {
        return sales.groupBy {it.product}
            .mapValues {(_, sales) ->
                sales.sumOf {it.quantity * it.pricePerUnit}}
            .maxByOrNull { it.value }?.key ?: "Нет продаж"
    }
}

fun main() {
    val sales = listOf(
        Sale("2025-10-01", "Ноутбук", 2, 69999.00),
        Sale("2025-10-15", "Телефон", 5, 49999.00),
        Sale("2025-11-02", "Ноутбук", 1, 69999.00),
        Sale("2025-11-20", "Наушники", 10, 7999.00),
        Sale("2025-10-05", "Телефон", 3, 49999.00)
    )
    val analyzer = SalesAnalyzer(sales)
    println("Общая выручка: $${analyzer.getTotalRevenue()}")
    println("Продажи по продуктам: ${analyzer.getSalesByProduct()}")
    println("Продажи за ноябрь: ${analyzer.getSalesByMonth("11")}")
    println("Топовый продукт: ${analyzer.getTopProductByRevenue()}")
}
