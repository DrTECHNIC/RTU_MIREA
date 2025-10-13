class Food(
    override val name: String,
    override val basePrice: Double,
    val ingredients: List<Ingredient>
) : MenuItem() {

    val isVegetarian: Boolean
        get() = ingredients.none { it.isAllergen }

    override fun calculateFinalPrice(): Double
    {return basePrice}

    override fun toString(): String
    {return """
        Блюдо:
            Название = "$name"
            Базовая стоимость = ${"%.2f".format(basePrice)}
            Ингридиенты = $ingredients
            Аллергическое = $isVegetarian
            Итоговая стоимость = ${"%.2f".format(calculateFinalPrice())}
        """.trimIndent()}
}
