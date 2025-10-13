fun main() {
    val menu = mutableListOf<MenuItem>()

    while (true) {
        println("\n=== Система заказов в кафе ===")
        println("1. Добавить напиток")
        println("2. Добавить блюдо")
        println("3. Показать меню")
        println("4. Рассчитать общую сумму заказа")
        println("5. Выход")
        print("Выберите действие: ")

        when (readLine()) {
            "1" -> addDrink(menu)
            "2" -> addFood(menu)
            "3" -> showMenu(menu)
            "4" -> calculateTotal(menu)
            "5" -> break
            else -> println("Неверный ввод")
        }
    }
}

fun addDrink(menu: MutableList<MenuItem>) {
    println("\nДобавление напитка:")
    print("Введите название: ")
    val name = readLine() ?: ""

    print("Введите базовую цену: ")
    val price = readLine()?.toDoubleOrNull() ?: 0.0

    println("Выберите размер:")
    println("1. SMALL")
    println("2. MEDIUM")
    println("3. LARGE")
    print("Ваш выбор: ")

    val size = when (readLine()) {
        "1" -> Size.SMALL
        "2" -> Size.MEDIUM
        "3" -> Size.LARGE
        else -> Size.MEDIUM
    }

    val drink = Drink(name, price, size)
    menu.add(drink)
    println("Напиток добавлен: $drink")
}

fun addFood(menu: MutableList<MenuItem>) {
    println("\nДобавление блюда:")
    print("Введите название: ")
    val name = readLine() ?: ""

    print("Введите базовую цену: ")
    val price = readLine()?.toDoubleOrNull() ?: 0.0

    val ingredients = mutableListOf<Ingredient>()
    println("Добавление ингредиентов (для завершения введите пустую строку):")

    while (true) {
        print("Название ингредиента: ")
        val ingName = readLine() ?: ""
        if (ingName.isEmpty()) break

        print("Является аллергеном? (д/н): ")
        val isAllergen = readLine()?.equals("д", ignoreCase = true) ?: false

        ingredients.add(Ingredient(ingName, isAllergen))
    }

    val food = Food(name, price, ingredients)
    menu.add(food)
    println("Блюдо добавлено: $food")
}

fun showMenu(menu: List<MenuItem>) {
    println("\n=== МЕНЮ ===")
    if (menu.isEmpty()) {
        println("Меню пустое")
        return
    }

    menu.forEachIndexed { index, item ->
        println("${index + 1}. $item")
    }
}

fun calculateTotal(menu: List<MenuItem>) {
    val total = menu.sumOf { it.calculateFinalPrice() }
    println("\nОбщая сумма заказа: $total")
}
