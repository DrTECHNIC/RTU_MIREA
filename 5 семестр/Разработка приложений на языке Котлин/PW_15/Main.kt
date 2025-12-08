fun main() {
    println("1. Создание последовательности из 10–15 городов с разными показателями качества воздуха.")
    val cities = createCitiesSequence().toList()
    println(cities.forEach { println("    $it")
    })
    println()

    println("2. Фильтрацию по уровню – выбрать города, где PM2.5 > 50 (опасный уровень).")
    val dangerousCities = filterDangerousCities(cities.asSequence())
    dangerousCities.forEach { println("   - ${it.city} (${it.country}): ${it.pm25}") }
    println()

    println("3. Проверку безопасности – проверить, все ли города в определенной стране имеют PM10 < 100.")
    listOf("Страна_1", "Страна_2", "Страна_3").forEach { country ->
        val isSafe = isCountrySafeForPM10(cities, country)
        println("   - $country: ${if (isSafe) "безопасно" else "опасно"}")
    }
    println()

    println("4. Трансформацию в статистику – преобразовать данные в строку: «Город: [city], PM2.5: [pm25], Статус: \${if(pm25 > 50) \"Опасно\" else \"Нормально\"}»")
    transformToStatistics(cities.asSequence()).forEach { println("   - $it") }
    println()

    println("5. Группировку города по странам.")
    val grouped = groupCitiesByCountry(cities.asSequence())
    grouped.forEach { (country, cityList) ->
        println("   - $country: ${cityList.size} города")
    }
    println()

    println("6. Сортировку города по убыванию PM2.5.")
    val sorted = sortCitiesByPM25(cities.asSequence())
    sorted.forEachIndexed { index, city ->
        println("   ${index + 1}. ${city.city}: ${city.pm25}")
    }
    println()

    println("7. Расчет для каждой страны средний PM2.5 и PM10.")
    calculateCountryAverages(cities.asSequence()).forEach {
        println("   - ${it.country}: PM2.5=${"%.1f".format(it.avgPM25)}, PM10=${"%.1f".format(it.avgPM10)}")
    }
    println()
}
