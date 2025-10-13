fun main() {
    val coffee = Drink("Кофе", 100.0, Size.LARGE)
    val tea = Drink("Чай", 80.0, Size.MEDIUM)
    val salad = Food("Салат", 150.0, listOf(
        Ingredient("Овощи", false),
        Ingredient("Орехи", true)
    ))
    val pasta = Food("Паста", 180.0, listOf(
        Ingredient("Паста", false),
        Ingredient("Соус", false)
    ))
    val menu = listOf(coffee, tea, salad, pasta)

    println("МЕНЮ:")
    menu.forEach { println(it) }

    println("\nДЕМОНСТРАЦИЯ:")
    val smallDrink = Drink("Пиво (маленькое)", 100.0, Size.SMALL)
    val largeDrink = Drink("Пиво (большое)", 100.0, Size.LARGE)
    println("$smallDrink\n\n$largeDrink")
    val total = menu.sumOf { it.calculateFinalPrice() }
    println("\nОбщая стоимость: ${"%.2f".format(total)}")
    println("ID первого элемента: ${menu.first().id}")
}