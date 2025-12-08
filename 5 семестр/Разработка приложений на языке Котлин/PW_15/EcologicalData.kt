data class CityAirQuality(
    val city: String,
    val country: String,
    val pm25: Int, // концентрация PM2.5
    val pm10: Int,
    val lastUpdate: String
)

fun createCitiesSequence(): Sequence<CityAirQuality> {
    return sequenceOf(
        CityAirQuality("Город_1", "Страна_1", 65, 110, "2025-12-08"),
        CityAirQuality("Город_2", "Страна_1", 45, 85, "2025-12-08"),
        CityAirQuality("Город_3", "Страна_2", 180, 250, "2025-12-08"),
        CityAirQuality("Город_4", "Страна_3", 120, 180, "2025-12-08"),
        CityAirQuality("Город_5", "Страна_4", 35, 60, "2025-12-08"),
        CityAirQuality("Город_6", "Страна_4", 55, 90, "2025-12-08"),
        CityAirQuality("Город_7", "Страна_5", 25, 45, "2025-12-08"),
        CityAirQuality("Город_8", "Страна_6", 40, 70, "2025-12-08"),
        CityAirQuality("Город_9", "Страна_7", 30, 55, "2025-12-08"),
        CityAirQuality("Город_10", "Страна_1", 95, 150, "2025-12-08"),
        CityAirQuality("Город_11", "Страна_7", 70, 120, "2025-12-08"),
        CityAirQuality("Город_12", "Страна_3", 50, 95, "2025-12-08"),
        CityAirQuality("Город_13", "Страна_3", 110, 190, "2025-12-08"),
        CityAirQuality("Город_14", "Страна_4", 38, 65, "2025-12-08"),
        CityAirQuality("Город_15", "Страна_2", 22, 40, "2025-12-08")
    )
}

fun filterDangerousCities(cities: Sequence<CityAirQuality>): List<CityAirQuality> {
    return cities.filter { it.pm25 > 50 }.toList()
}

fun isCountrySafeForPM10(cities: List<CityAirQuality>, country: String): Boolean {
    return cities
        .filter { it.country == country }
        .all { it.pm10 < 100 }
}

fun transformToStatistics(cities: Sequence<CityAirQuality>): List<String> {
    return cities.map { city ->
        "Город: ${city.city}, PM2.5: ${city.pm25}, Статус: ${if (city.pm25 > 50) "Опасно" else "Нормально"}"
    }.toList()
}

fun groupCitiesByCountry(cities: Sequence<CityAirQuality>): Map<String, List<CityAirQuality>> {
    return cities.groupBy { it.country }
}

fun sortCitiesByPM25(cities: Sequence<CityAirQuality>): List<CityAirQuality> {
    return cities.sortedByDescending { it.pm25 }.toList()
}

data class CountryAverages(
    val country: String,
    val avgPM25: Double,
    val avgPM10: Double
)

fun calculateCountryAverages(cities: Sequence<CityAirQuality>): List<CountryAverages> {
    return cities
        .groupBy { it.country }
        .map { (country, cityList) ->
            val avgPM25 = cityList.map { it.pm25 }.average()
            val avgPM10 = cityList.map { it.pm10 }.average()
            CountryAverages(country, avgPM25, avgPM10)
        }
}
