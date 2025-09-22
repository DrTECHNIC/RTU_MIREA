fun main() {
    val menu = {
        println("1. Играть в \"Поле чудес\"")
        println("2. Вывести k самых частых слов")
        println("0. Выход")
        print("Выберите опцию: ")
    }
    while (true) {
        menu()
        when (readlnOrNull()?.toIntOrNull()) {
            1 -> task1()
            2 -> task2()
            0 -> return
            else -> println("Неверная опция")
        }
    }
}

fun task1() {
    println("\"Поле чудес\"!")
    val words = listOf("ПРОГРАММИРОВАНИЕ", "КОТЛИН", "ПРИЛОЖЕНИЕ", "КОМПЬЮТЕР", "ТЕЛЕФОН",
        "АНДРОИД", "ДИСПЛЕЙ", "ЭКРАН", "УПРАВЛЕНИЕ", "ИГРА", "ПРОГРАММИСТ", "УНИВЕРСИТЕТ",
        "КЛАВИАТУРА", "МОНИТОР", "ФОТОАППАРАТ", "ТЕХНОЛОГИЯ", "ТЕХНИКА", "УЛЫБКА", "ВЛИЯНИЕ",
        "ЭСПРЕССО", "ЧАЙ", "КОФЕ", "ПАРАЛЛЕЛИПИПЕД", "СТОЛОВАЯ", "КАБИНЕТ", "АУДИТОРИЯ",
        "ТЕЛЕГРАМ", "ВКОНТАКТЕ", "БЛЕНДЕР", "ДЕВУШКА", "ПАРЕНЬ", "МУЖЧИНА", "ЖЕНЩИНА",
        "МАЛЬЧИК", "ДЕВОЧКА", "ДЕДУШКА", "БАБУШКА", "ВОЕННОСЛУЖАЩИЙ", "НЕЙРОСЕТЬ", "МОДЕЛИРОВАНИЕ",
        "РОБОТИЗАЦИЯ", "РОБОТ", "КНИГА", "ПИСЬМО", "РЕПОЗИТОРИЙ", "ШКОЛЬНИК", "СТУДЕНТ", "РАБОЧИЙ")
    val secretWord = words.random()
    var displayedWord = "*".repeat(secretWord.length)
    var mistakes = 0
    val maxMistakes = 10
    while (mistakes < maxMistakes && displayedWord.contains('*')) {
        println("\nСлово: $displayedWord")
        print("Введите букву: ")
        val input = readlnOrNull()?.uppercase()?.take(1)
        if (input.isNullOrEmpty() || !input[0].isLetter()) {
            println("Некорректный ввод!")
            continue
        }
        val guess = input[0]
        val newDisplay = secretWord.foldIndexed(StringBuilder()) { idx, sb, c ->
            sb.append(if (c == guess) c else displayedWord[idx])
        }.toString()
        if (newDisplay == displayedWord) {
            mistakes++
            println("Ошибка! Осталось попыток: ${maxMistakes - mistakes}")
        } else {
            displayedWord = newDisplay
            println("Есть такая буква!")
        }
    }
    println(
        if (mistakes == maxMistakes)
            "Вы проиграли! Загаданное слово: $secretWord"
        else
            "Поздравляем! Вы отгадали слово: $secretWord"
    )
}

fun task2() {
    print("Введите слова через пробел: ")
    val words = readlnOrNull()?.split(" ")?.filter { it.isNotBlank() } ?: emptyList()
    print("Введите число k: ")
    val k = readlnOrNull()?.toIntOrNull() ?: 0
    if (k <= 0) {
        println("Некорректное значение k!")
        return
    }
    val find: (List<String>, Int) -> List<String> = { words, k ->
        words.groupingBy { it }
            .eachCount()
            .entries
            .sortedWith(compareByDescending<Map.Entry<String, Int>> { it.value }
                .thenByDescending { it.key })
            .take(k)
            .map { it.key }
    }
    val result = find(words, k)
    println("Результат: ${result.joinToString()}")
}