enum class Size { SMALL, MEDIUM, LARGE }

class Drink(
    override val name: String,
    override val basePrice: Double,
    val size: Size
) : MenuItem() {

    final override fun calculateFinalPrice(): Double {
        return when (size) {
            Size.SMALL -> basePrice * 1.0
            Size.MEDIUM -> basePrice * 1.5
            Size.LARGE -> basePrice * 2.0
        }
    }

    override fun toString(): String
    {return """
        Напиток:
            Название = "$name"
            Базовая стоимость = ${"%.2f".format(basePrice)}
            Размер = $size
            Итоговая стоимость = ${"%.2f".format(calculateFinalPrice())}
        """.trimIndent()}
}
