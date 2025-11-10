import java.util.UUID

abstract class MenuItem {
    abstract val name: String
    abstract val basePrice: Double
    val id: String = UUID.randomUUID().toString()

    abstract fun calculateFinalPrice(): Double
}
