enum class DrinkType(
    private val displayName: String,
    private val drinkVolume: Int,
    private val temperature: Int,
) {
    Coffee("кофе", 120, 80),
    Tea("чай", 150, 40),
    Juice("сок", 900, 5),
    Water("вода", 1500, 15),;

    fun getFormattedName(): String {return displayName.replaceFirstChar {it.uppercase()}}
    fun getVolume(): Int = drinkVolume
    fun isHot(): Boolean = temperature > 60
}

fun main() {
    DrinkType.entries.forEach { drink ->
        println("Напиток: ${drink.getFormattedName()}")
        println("Объем: ${drink.getVolume()} мл")
        println("Горячий: ${if (drink.isHot()) "Да" else "Нет"}\n")
    }
}
