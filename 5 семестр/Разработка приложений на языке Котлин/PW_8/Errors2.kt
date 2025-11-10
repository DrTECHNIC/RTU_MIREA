open class Animal {
    // open
    open fun speak() = "Some sound"
}

class Cat : Animal() {
    override fun speak() = "Meow!"
}

fun main() {
    val cat = Cat()
    println(cat.speak())
}
