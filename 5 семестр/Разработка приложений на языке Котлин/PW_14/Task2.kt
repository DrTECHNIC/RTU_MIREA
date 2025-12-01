import java.util.Scanner

object Task2 {
    private val entries = listOf(
        mapOf(
            "text" to "❝ Фира! Все. Антракт! Хватит греть уши! ❞",
            "author" to "Жизнь и приключения Мишки Япончика (Однажды в Одессе)",
            "type" to "quote",
            "tags" to listOf("фильм", "одесса", "юмор", "криминал")
        ),
        mapOf(
            "text" to "❝ Честность и трудолюбие хоть кого поставят на ноги. ❞",
            "author" to "Ганс Кристиан Андерсен",
            "type" to "quote",
            "tags" to listOf("труд", "честность", "мораль", "сказка")
        ),
        mapOf(
            "text" to "❝ Если усложнить ложь, она всё равно не станет правдой. ❞",
            "author" to "Бэкстром (Backstrom)",
            "type" to "quote",
            "tags" to listOf("правда", "ложь", "детектив", "философия")
        ),
        mapOf(
            "text" to "❝ Любовь — это игра в карты, в которой блефуют оба: один, чтобы выиграть, другой, чтобы не проиграть. ❞",
            "author" to "Анри Ренье",
            "type" to "quote",
            "tags" to listOf("любовь", "отношения", "игра", "философия")
        ),
        mapOf(
            "text" to "❝ Все мы выдаем себя не за тех, кем являемся на деле. Мы стараемся быть значительнее, остроумнее перед женщиной, если она нам нравится. Мы стараемся быть умнее перед мужчинами, добрее перед стариками, благоразумнее перед начальниками. Мы играем разные роли, иногда по десяти раз на дню. ❞",
            "author" to "Кир Булычев",
            "type" to "quote",
            "tags" to listOf("психология", "общество", "роли", "философия")
        ),
        mapOf(
            "text" to "❝ Это что — все не мне??... Не дам!! ❞",
            "author" to "Маша и медведь",
            "type" to "quote",
            "tags" to listOf("мультфильм", "детское", "юмор", "жадность")
        ),
        mapOf(
            "text" to "❝ Недостаточно быть умным. Необходимо быть достаточно умным, чтобы не позволить себе стать умным сверх меры. ❞",
            "author" to "Андре Моруа",
            "type" to "quote",
            "tags" to listOf("мудрость", "интеллект", "скромность", "философия")
        ),
        mapOf(
            "text" to "❝ Одиночество лишь умножает печаль. ❞",
            "author" to "Город, в котором меня нет (Boku dake ga Inai Machi)",
            "type" to "quote",
            "tags" to listOf("одиночество", "печаль", "аниме", "психология")
        ),
        mapOf(
            "text" to "❝ Есть стратегия, а есть тактика. Это была тактическая операция. А то, что целый батальон полег, — это дело десятое. Как говорил товарищ Сталин — смерть одного человека — трагедия, а смерть тысяч — статистика. ❞",
            "author" to "Штрафбат",
            "type" to "quote",
            "tags" to listOf("война", "стратегия", "статистика", "драма")
        ),
        mapOf(
            "text" to "❝ Есть три разновидности лжи: ложь, гнусная ложь и статистика. ❞",
            "author" to "Бенджамин Дизраэли",
            "type" to "quote",
            "tags" to listOf("статистика", "ложь", "политика", "философия")
        ),
        mapOf(
            "text" to "❝ Мы — это всего лишь наши воспоминания. ❞",
            "author" to "Дэвид Митчелл",
            "type" to "quote",
            "tags" to listOf("память", "личность", "философия", "литература")
        ),
        mapOf(
            "text" to "❝ Если тебя все время напрягает прошлое – это твоя вина, потому что ты не умеешь жить настоящим. ❞",
            "author" to "Крутой учитель Онидзука (Great Teacher Onizuka)",
            "type" to "quote",
            "tags" to listOf("прошлое", "настоящее", "аниме", "психология")
        ),
        mapOf(
            "text" to "❝ Характер человека никогда нельзя понять вернее, чем по той шутке, на которую он обижается. ❞",
            "author" to "Георг Кристоф Лихтенберг",
            "type" to "quote",
            "tags" to listOf("характер", "юмор", "психология", "философия")
        ),
        mapOf(
            "text" to "❝ Как можно в дружбу с недругом вступить? Холодный ветер из огня добыть? С какой бы ни пришел ты добротою, Вовеки будет враг дышать враждою. ❞",
            "author" to "Абулькасим Фирдоуси. Шахнаме",
            "type" to "quote",
            "tags" to listOf("дружба", "враги", "поэзия", "философия")
        ),
        mapOf(
            "text" to "❝ Молчание иногда говорит больше, чем слова, просто нужно научиться его понимать. ❞",
            "author" to "Хелен Тодд. Люфт",
            "type" to "quote",
            "tags" to listOf("молчание", "общение", "психология", "литература")
        ),

        mapOf(
            "text" to "Превед, медвед!",
            "author" to "Russian Internet Meme",
            "type" to "meme",
            "tags" to listOf("интернет", "олбанский", "ранний интернет", "юмор")
        ),
        mapOf(
            "text" to "Йоу, чо надо? Йоу, чо надо?",
            "author" to "Наша Russia",
            "type" to "meme",
            "tags" to listOf("сериал", "рашен", "юмор", "интернет")
        ),
        mapOf(
            "text" to "Я у мамы дурочка",
            "author" to "Реальные пацаны",
            "type" to "meme",
            "tags" to listOf("сериал", "юмор", "мама", "интернет")
        ),
        mapOf(
            "text" to "Это фиаско, братан",
            "author" to "Russian Internet Meme",
            "type" to "meme",
            "tags" to listOf("неудача", "юмор", "интернет", "разочарование")
        ),
        mapOf(
            "text" to "Денег нет, но вы держитесь",
            "author" to "Дмитрий Медведев",
            "type" to "meme",
            "tags" to listOf("политика", "экономика", "юмор", "интернет")
        ),
        mapOf(
            "text" to "This is fine",
            "author" to "American Internet Meme",
            "type" to "meme",
            "tags" to listOf("сатира", "апатия", "интернет", "юмор")
        ),
        mapOf(
            "text" to "One does not simply walk into Mordor",
            "author" to "Lord of the Rings Meme",
            "type" to "meme",
            "tags" to listOf("фэнтези", "кино", "интернет", "юмор")
        ),
        mapOf(
            "text" to "Distracted Boyfriend",
            "author" to "American Internet Meme",
            "type" to "meme",
            "tags" to listOf("измена", "отношения", "юмор", "интернет")
        ),
        mapOf(
            "text" to "Woman Yelling at a Cat",
            "author" to "American Internet Meme",
            "type" to "meme",
            "tags" to listOf("кот", "ссора", "юмор", "интернет")
        ),
        mapOf(
            "text" to "Always has been",
            "author" to "Space Meme",
            "type" to "meme",
            "tags" to listOf("космос", "предательство", "юмор", "интернет")
        ),

        mapOf(
            "text" to "Томный вечер смотрит в окна",
            "author" to "Николай Степанович Власов-Окский",
            "type" to "poem",
            "tags" to listOf("одиночество", "вечер", "любовь", "тоска")
        ),
        mapOf(
            "text" to "Как хорошо здесь отдохнуть от слов",
            "author" to "Вера Сергеевна Булич",
            "type" to "poem",
            "tags" to listOf("природа", "деревья", "тишина", "мудрость")
        ),
        mapOf(
            "text" to "Чу! Ширь глухая вдруг завыла!",
            "author" to "Юргис Казимирович Балтрушайтис",
            "type" to "poem",
            "tags" to listOf("метель", "зима", "природа", "буря")
        ),
        mapOf(
            "text" to "Я не ропщу. Я вознесен судьбою",
            "author" to "Денис Васильевич Давыдов",
            "type" to "poem",
            "tags" to listOf("любовь", "ревность", "счастье", "романтика")
        ),
        mapOf(
            "text" to "Мы не живем - мы спорим",
            "author" to "Варвара Александровна Монина",
            "type" to "poem",
            "tags" to listOf("религия", "страдание", "война", "философия")
        ),
        mapOf(
            "text" to "Есть книга чудная, где с каждою страницей",
            "author" to "Иннокентий Фёдорович Анненский",
            "type" to "poem",
            "tags" to listOf("музыка", "мечта", "искусство", "мистика")
        ),
        mapOf(
            "text" to "Не рассуждай, не хлопочи!..",
            "author" to "Фёдор Иванович Тютчев",
            "type" to "poem",
            "tags" to listOf("философия", "жизнь", "принятие", "мудрость")
        ),
        mapOf(
            "text" to "Был трудный бой. Всё нынче, как спросонку",
            "author" to "Александр Трифонович Твардовский",
            "type" to "poem",
            "tags" to listOf("война", "память", "героизм", "дети")
        ),
        mapOf(
            "text" to "Много есть персиянок на свете",
            "author" to "Николай Яковлевич Агнивцев",
            "type" to "poem",
            "tags" to listOf("любовь", "юмор", "восток", "ирония")
        ),
        mapOf(
            "text" to "Сажень земли мое стяжанье",
            "author" to "Вильгельм Карлович Кюхельбекер",
            "type" to "poem",
            "tags" to listOf("смерть", "забвение", "философия", "кладбище")
        ),
        mapOf(
            "text" to "Шел по лесу дед Мороз",
            "author" to "Зинаида Николаевна Александрова",
            "type" to "poem",
            "tags" to listOf("новый год", "зима", "дед мороз", "детское")
        ),
        mapOf(
            "text" to "Так Солнце некогда расспорилось с Луною",
            "author" to "Василий Иванович Майков",
            "type" to "poem",
            "tags" to listOf("басня", "солнце", "луна", "слава")
        ),
        mapOf(
            "text" to "Дама, качаясь на ветке",
            "author" to "Саша Чёрный",
            "type" to "poem",
            "tags" to listOf("сатира", "детская поэзия", "юмор", "ирония")
        )
    )

    fun filterByType(type: String): List<Map<String, Any>> {
        return entries.filter { it["type"] == type }
    }

    fun findByAuthor(author: String): List<Map<String, Any>> {
        return entries.filter { (it["author"] as String).equals(author, ignoreCase = true) }
    }

    fun findByTag(tag: String): List<Map<String, Any>> {
        return entries.filter { entry -> (entry["tags"] as List<String>).any { it.equals(tag, ignoreCase = true) } }
    }

    fun getStatistics(): Pair<Set<String>, Set<String>> {
        val allAuthors = entries.map { it["author"] as String }.toSet()
        val allTags = entries.flatMap { it["tags"] as List<String> }.toSet()
        return Pair(allAuthors, allTags)
    }

    fun groupByType(): Map<String, List<Map<String, Any>>> {
        return entries.groupBy { it["type"] as String }
    }

    private fun printEntry(entry: Map<String, Any>, index: Int = -1) {
        if (index != -1) print("$index. ")
        when (entry["type"]) {
            "quote" -> println("ЦИТАТА:")
            "poem" -> println("СТИХОТВОРЕНИЕ:")
            "meme" -> println("МЕМ:")
        }
        val text = entry["text"] as String
        println("   \"${text.take(100)}${if (text.length > 100) "..." else ""}\"")
        println("   Автор: ${entry["author"]}")
        println("   Теги: ${(entry["tags"] as List<String>).joinToString(", ")}")
        println()
    }

    fun run() {
        val scanner = Scanner(System.`in`)
        var exit = false
        println("Всего записей: ${entries.size}")
        println("  • Цитат: ${filterByType("quote").size}")
        println("  • Стихотворений: ${filterByType("poem").size}")
        println("  • Мемов: ${filterByType("meme").size}")
        while (!exit) {
            println("\n" + "=".repeat(50))
            println("МЕНЮ:")
            println("1. Показать все записи")
            println("2. Фильтрация по типу (quote/poem/meme)")
            println("3. Поиск по автору")
            println("4. Поиск по тегу")
            println("5. Статистика")
            println("6. Группировка по типу")
            println("7. Показать краткую информацию")
            println("0. Выход")
            print("Выберите действие: ")
            when (scanner.nextLine().toIntOrNull()) {
                1 -> {
                    entries.forEachIndexed {index, entry ->
                        printEntry(entry, index + 1)
                        if ((index + 1) % 5 == 0) {
                            print("Нажмите Enter для продолжения")
                            scanner.nextLine()
                        }
                    }
                }
                2 -> {
                    print("Введите тип (quote/poem/meme): ")
                    val type = scanner.nextLine().lowercase()
                    val filtered = filterByType(type)
                    if (filtered.isEmpty()) println("Записей с типом '$type' не найдено")
                    else filtered.forEachIndexed {index, entry -> printEntry(entry, index + 1)}
                }
                3 -> {
                    print("Введите автора: ")
                    val author = scanner.nextLine()
                    val found = findByAuthor(author)
                    if (found.isEmpty()) println("Записей автора '$author' не найдено")
                    else found.forEachIndexed {index, entry -> printEntry(entry, index + 1)}
                }
                4 -> {
                    print("Введите тег: ")
                    val tag = scanner.nextLine()
                    val found = findByTag(tag)
                    if (found.isEmpty()) println("Записей с тегом '$tag' не найдено")
                    else found.forEachIndexed {index, entry -> printEntry(entry, index + 1)}
                }
                5 -> {
                    val (authors, tags) = getStatistics()
                    println("Уникальные авторы (${authors.size}):")
                    authors.sorted().forEach {println("  • $it")}
                    println("\nУникальные теги (${tags.size}):")
                    tags.sorted().forEach {println("  • $it")}
                }
                6 -> {
                    val grouped = groupByType()
                    grouped.forEach {(type, entriesList) ->
                        val typeName = when (type) {
                            "quote" -> "Цитаты"
                            "poem" -> "Стихотворения"
                            "meme" -> "Мемы"
                            else -> type
                        }
                        println("\n$typeName (${entriesList.size} записей)")
                        println("-".repeat(40))
                        entriesList.take(3).forEach {
                                entry -> println("  • \"${(entry["text"] as String).take(50)}...\" - ${entry["author"]}")}
                        if (entriesList.size > 3) println("  ... и еще ${entriesList.size - 3} записей")
                    }
                }
                7 -> {
                    println("Всего записей: ${entries.size}")
                    val grouped = groupByType()
                    grouped.forEach { (type, list) ->
                        val typeName = when (type) {
                            "quote" -> "Цитаты"
                            "poem" -> "Стихотворения"
                            "meme" -> "Мемы"
                            else -> type
                        }
                        println("$typeName: ${list.size}")
                    }
                    val tagCounts = entries.flatMap {it["tags"] as List<String>}
                        .groupingBy {it}
                        .eachCount()
                        .toList()
                        .sortedByDescending {it.second}
                        .take(5)
                    println("\nТоп-5 популярных тегов:")
                    tagCounts.forEachIndexed {index, (tag, count) -> println("${index + 1}. $tag ($count записей)")}
                }
                0 -> exit = true
                else -> println("Неверный ввод. Попробуйте еще раз.")
            }
        }
    }
}
