fun encodeToMorse() {
    val morseCodes = arrayOf(
        ".-", "-...", ".--", "--.", "-..", ".", "...-", "--..", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", ".-.", "...", "-", "..-",
        "..-.", "....", "-.-.", "---.", "----", "--.-", "--.--", "-.--", "-..-",
        "..-..", "..--", ".-.-"
    )

    print("Введите строку из русских заглавных букв (без Ё): ")
    val input = readLine()?.takeIf { it.isNotEmpty() } ?: run {
        println("Пустая строка!")
        return
    }

    if (!input.matches(Regex("^[А-Я]+$"))) {
        println("Ошибка: допускаются только русские заглавные буквы (без Ё)")
        return
    }

    val result = StringBuilder()
    for (char in input) {
        val index = char - 'А'
        result.append(morseCodes[index]).append(" ")
    }
    println("Результат: ${result.trim()}")
}

fun main() {
    encodeToMorse()
}