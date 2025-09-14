fun generatePassword() {
    val uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val lowercase = "abcdefghijklmnopqrstuvwxyz"
    val digits = "0123456789"
    val specials = "_*-"
    val allChars = uppercase + lowercase + digits + specials

    var n: Int
    while (true) {
        print("Введите длину пароля (N >= 8): ")
        n = readLine()?.toIntOrNull() ?: -1

        when {
            n < 8 -> println("Пароль с $n количеством символов небезопасен")
            else -> break
        }
    }

    val password = StringBuilder().apply {
        append(uppercase.random())
        append(lowercase.random())
        append(digits.random())
        append(specials.random())
        repeat(n - 4) { append(allChars.random()) }
    }.toString().toList().shuffled().joinToString("")

    println("Сгенерированный пароль: $password")
}

fun main() {
    generatePassword()
}