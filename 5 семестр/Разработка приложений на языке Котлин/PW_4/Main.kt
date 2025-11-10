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
    fun isValidInput(input: String?) = input != null && input.isNotEmpty() && input[0].isLetter()
    val processLetter: (Char) -> Unit = { letter ->
        val newChars = displayedWord.toCharArray()
        var found = false
        for (i in secretWord.indices)
            if (secretWord[i] == letter) {
                newChars[i] = letter
                found = true
            }
        if (found) {
            displayedWord = String(newChars)
            println("Есть такая буква!")
        } else {
            mistakes++
            println("Ошибка! Осталось попыток: ${maxMistakes - mistakes}")
        }
    }
    while (mistakes < maxMistakes && displayedWord.contains('*')) {
        println("\nСлово: $displayedWord")
        print("Введите букву: ")
        val input = readlnOrNull()?.uppercase()?.take(1)
        if (!isValidInput(input)) {
            println("Некорректный ввод!")
            continue
        }
        processLetter(input!![0])
    }
    val resultMessage = if (mistakes == maxMistakes)
        "Вы проиграли! Загаданное слово: $secretWord"
    else
        "Поздравляем! Вы отгадали слово: $secretWord"
    println(resultMessage)
}

fun task2() {
    print("Введите слова через пробел: ")
    val inputLine = readlnOrNull() ?: ""
    val inputWords = mutableListOf<String>()
    for (word in inputLine.split(" "))
        if (word.isNotBlank())
            inputWords.add(word)
    print("Введите число k: ")
    val k = readlnOrNull()?.toIntOrNull() ?: 0
    if (k <= 0) {
        println("Некорректное значение k!")
        return
    }
    val frequencyMap = mutableMapOf<String, Int>()
    for (word in inputWords)
        frequencyMap[word] = frequencyMap.getOrDefault(word, 0) + 1
    val entries = mutableListOf<Map.Entry<String, Int>>()
    for (entry in frequencyMap.entries)
        entries.add(entry)
    val sortByFrequency: (MutableList<Map.Entry<String, Int>>) -> Unit = { list ->
        for (i in 0 until list.size - 1)
            for (j in 0 until list.size - i - 1) {
                val current = list[j]
                val next = list[j + 1]
                if (current.value < next.value || (current.value == next.value && current.key < next.key)) {
                    val temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
                }
            }
    }
    sortByFrequency(entries)
    val topWords = mutableListOf<String>()
    val count = if (k < entries.size) k else entries.size
    for (i in 0 until count)
        topWords.add(entries[i].key)
    println("Результат: ${topWords.joinToString()}")
}