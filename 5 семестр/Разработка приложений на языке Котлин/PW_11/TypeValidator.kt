class ValueValidator<T : Any> {
    fun validate(value: T): Boolean {
        return when (value) {
            is Int -> value > 0
            is Double -> value > 0.0
            is String -> value.length > 5
            else -> throw IllegalArgumentException("Unsupported type: ${value::class.simpleName}")
        }
    }
}

fun main() {
    val validator = ValueValidator<Any>()
    println(validator.validate(10))
    println(validator.validate(-5))
    println(validator.validate(3.14))
    println(validator.validate(-2.5))
    println(validator.validate("short"))
    println(validator.validate("valid string"))
    try {
        println(validator.validate(true))
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}