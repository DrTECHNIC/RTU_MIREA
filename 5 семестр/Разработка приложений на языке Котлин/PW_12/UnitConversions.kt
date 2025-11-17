import kotlin.math.PI

fun Double.celsiusToFahrenheit() = this * 9.0 / 5.0 + 32
fun Double.fahrenheitToCelsius() = (this - 32) * 5.0 / 9.0
fun Double.celsiusToKelvin() = this + 273.15
fun Double.kelvinToCelsius() = this - 273.15

fun Double.kilogramsToPounds() = this * 2.20462
fun Double.poundsToKilograms() = this / 2.20462
fun Double.gramsToOunces() = this * 0.035274
fun Double.ouncesToGrams() = this / 0.035274

fun Double.minutesToSeconds() = this * 60
fun Double.secondsToMinutes() = this / 60
fun Double.hoursToMinutes() = this * 60
fun Double.minutesToHours() = this / 60
fun Double.daysToHours() = this * 24
fun Double.hoursToDays() = this / 24
fun Double.weeksToDays() = this * 7
fun Double.daysToWeeks() = this / 7

fun Double.litersToGallons() = this * 0.264172
fun Double.gallonsToLiters() = this / 0.264172
fun Double.millilitersToCups() = this * 0.00422675
fun Double.cupsToMilliliters() = this / 0.00422675
fun Double.litersToCubicMeters() = this / 1000
fun Double.cubicMetersToLiters() = this * 1000

fun Double.squareMetersToSquareFeet() = this * 10.7639
fun Double.squareFeetToSquareMeters() = this / 10.7639
fun Double.hectaresToAcres() = this * 2.47105
fun Double.acresToHectares() = this / 2.47105
fun Double.squareKilometersToSquareMiles() = this * 0.386102
fun Double.squareMilesToSquareKilometers() = this / 0.386102

fun Double.degreesToRadians() = this * PI / 180
fun Double.radiansToDegrees() = this * 180 / PI
fun Double.degreesToGradians() = this * 200.0 / 180.0
fun Double.gradiansToDegrees() = this * 180.0 / 200.0

fun Double.megabytesToGigabytes() = this / 1024
fun Double.gigabytesToMegabytes() = this * 1024
fun Double.gigabytesToTerabytes() = this / 1024
fun Double.terabytesToGigabytes() = this * 1024
fun Double.kilobytesToMegabytes() = this / 1024
fun Double.megabytesToKilobytes() = this * 1024

fun main() {
    while (true) {
        println("1. Температура")
        println("2. Вес")
        println("3. Время")
        println("4. Объем")
        println("5. Площадь")
        println("6. Углы")
        println("7. Цифровые данные")
        println("0. Выход")
        print("Выберите категорию: ")

        when (readLine()?.toIntOrNull()) {
            1 -> handleTemperatureConversion()
            2 -> handleWeightConversion()
            3 -> handleTimeConversion()
            4 -> handleVolumeConversion()
            5 -> handleAreaConversion()
            6 -> handleAngleConversion()
            7 -> handleDigitalDataConversion()
            0 -> return
            else -> println("Неверный ввод! Попробуйте снова.")
        }
    }
}

fun getInputValue(value: String): Double {
    while (true) {
        print(value)
        return readLine()?.toDoubleOrNull() ?: run {
            println("Ошибка! Введите числовое значение.")
            continue
        }
    }
}

fun getUnitSelection(selection: String, maxOption: Int): Int {
    while (true) {
        print(selection)
        val input = readLine()?.toIntOrNull()
        if (input != null && input in 1..maxOption) return input
        else println("Ошибка! Введите число от 1 до $maxOption.")
    }
}

fun handleTemperatureConversion() {
    println("Доступные единицы измерения:")
    println("1. Цельсий (°C)")
    println("2. Фаренгейт (°F)")
    println("3. Кельвин (K)")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 3)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 3)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val result = when {
        fromUnit == 1 && toUnit == 2 -> value.celsiusToFahrenheit()
        fromUnit == 1 && toUnit == 3 -> value.celsiusToKelvin()
        fromUnit == 2 && toUnit == 1 -> value.fahrenheitToCelsius()
        fromUnit == 2 && toUnit == 3 -> value.fahrenheitToCelsius().celsiusToKelvin()
        fromUnit == 3 && toUnit == 1 -> value.kelvinToCelsius()
        fromUnit == 3 && toUnit == 2 -> value.kelvinToCelsius().celsiusToFahrenheit()
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "°C"
        2 -> "°F"
        3 -> "K"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "°C"
        2 -> "°F"
        3 -> "K"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.2f".format(result)} $toUnitName")
}

fun handleWeightConversion() {
    println("Доступные единицы измерения:")
    println("1. Килограммы (кг)")
    println("2. Фунты")
    println("3. Граммы (г)")
    println("4. Унции")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 4)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 4)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val inKilograms = when (fromUnit) {
        1 -> value
        2 -> value.poundsToKilograms()
        3 -> value / 1000
        4 -> value.ouncesToGrams() / 1000
        else -> value
    }

    val result = when (toUnit) {
        1 -> inKilograms
        2 -> inKilograms.kilogramsToPounds()
        3 -> inKilograms * 1000
        4 -> inKilograms * 1000 * 0.035274
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "кг"
        2 -> "фунтов"
        3 -> "г"
        4 -> "унций"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "кг"
        2 -> "фунтов"
        3 -> "г"
        4 -> "унций"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.2f".format(result)} $toUnitName")
}

fun handleTimeConversion() {
    println("Доступные единицы измерения:")
    println("1. Часы")
    println("2. Минуты")
    println("3. Секунды")
    println("4. Дни")
    println("5. Недели")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 5)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 5)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val inHours = when (fromUnit) {
        1 -> value
        2 -> value.minutesToHours()
        3 -> value / 3600
        4 -> value * 24
        5 -> value.weeksToDays() * 24
        else -> value
    }

    val result = when (toUnit) {
        1 -> inHours
        2 -> inHours.hoursToMinutes()
        3 -> inHours * 3600
        4 -> inHours.hoursToDays()
        5 -> inHours.hoursToDays().daysToWeeks()
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "часов"
        2 -> "минут"
        3 -> "секунд"
        4 -> "дней"
        5 -> "недель"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "часов"
        2 -> "минут"
        3 -> "секунд"
        4 -> "дней"
        5 -> "недель"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.2f".format(result)} $toUnitName")
}

fun handleVolumeConversion() {
    println("Доступные единицы измерения:")
    println("1. Литры")
    println("2. Галлоны")
    println("3. Миллилитры")
    println("4. Чашки")
    println("5. Кубические метры")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 5)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 5)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val inLiters = when (fromUnit) {
        1 -> value
        2 -> value.gallonsToLiters()
        3 -> value / 1000
        4 -> value.cupsToMilliliters() / 1000
        5 -> value.cubicMetersToLiters()
        else -> value
    }

    val result = when (toUnit) {
        1 -> inLiters
        2 -> inLiters.litersToGallons()
        3 -> inLiters * 1000
        4 -> inLiters * 1000 * 0.00422675
        5 -> inLiters.litersToCubicMeters()
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "литров"
        2 -> "галлонов"
        3 -> "мл"
        4 -> "чашек"
        5 -> "м³"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "литров"
        2 -> "галлонов"
        3 -> "мл"
        4 -> "чашек"
        5 -> "м³"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.2f".format(result)} $toUnitName")
}

fun handleAreaConversion() {
    println("Доступные единицы измерения:")
    println("1. Квадратные метры (м²)")
    println("2. Квадратные футы")
    println("3. Гектары")
    println("4. Акры")
    println("5. Квадратные километры (км²)")
    println("6. Квадратные мили")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 6)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 6)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val inSquareMeters = when (fromUnit) {
        1 -> value
        2 -> value.squareFeetToSquareMeters()
        3 -> value * 10000
        4 -> value.acresToHectares() * 10000
        5 -> value * 1000000
        6 -> value.squareMilesToSquareKilometers() * 1000000
        else -> value
    }

    val result = when (toUnit) {
        1 -> inSquareMeters
        2 -> inSquareMeters.squareMetersToSquareFeet()
        3 -> inSquareMeters / 10000
        4 -> (inSquareMeters / 10000).hectaresToAcres()
        5 -> inSquareMeters / 1000000
        6 -> (inSquareMeters / 1000000).squareKilometersToSquareMiles()
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "м²"
        2 -> "кв. футов"
        3 -> "гектаров"
        4 -> "акров"
        5 -> "км²"
        6 -> "кв. миль"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "м²"
        2 -> "кв. футов"
        3 -> "гектаров"
        4 -> "акров"
        5 -> "км²"
        6 -> "кв. миль"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.2f".format(result)} $toUnitName")
}

fun handleAngleConversion() {
    println("Доступные единицы измерения:")
    println("1. Градусы (°)")
    println("2. Радианы")
    println("3. Грады")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 3)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 3)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val inDegrees = when (fromUnit) {
        1 -> value
        2 -> value.radiansToDegrees()
        3 -> value.gradiansToDegrees()
        else -> value
    }

    val result = when (toUnit) {
        1 -> inDegrees
        2 -> inDegrees.degreesToRadians()
        3 -> inDegrees.degreesToGradians()
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "°"
        2 -> "радиан"
        3 -> "градов"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "°"
        2 -> "радиан"
        3 -> "градов"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.4f".format(result)} $toUnitName")
}

fun handleDigitalDataConversion() {
    println("Доступные единицы измерения:")
    println("1. Килобайты (КБ)")
    println("2. Мегабайты (МБ)")
    println("3. Гигабайты (ГБ)")
    println("4. Терабайты (ТБ)")

    val fromUnit = getUnitSelection("Выберите исходную единицу измерения: ", 4)
    val toUnit = getUnitSelection("Выберите целевую единицу измерения: ", 4)

    if (fromUnit == toUnit) {
        println("Исходная и целевая единицы совпадают!")
        return
    }

    val value = getInputValue("Введите значение для конвертации: ")

    val inMegabytes = when (fromUnit) {
        1 -> value.kilobytesToMegabytes()
        2 -> value
        3 -> value.gigabytesToMegabytes()
        4 -> value.terabytesToGigabytes().gigabytesToMegabytes()
        else -> value
    }

    val result = when (toUnit) {
        1 -> inMegabytes.megabytesToKilobytes()
        2 -> inMegabytes
        3 -> inMegabytes.megabytesToGigabytes()
        4 -> inMegabytes.megabytesToGigabytes().gigabytesToTerabytes()
        else -> value
    }

    val fromUnitName = when (fromUnit) {
        1 -> "КБ"
        2 -> "МБ"
        3 -> "ГБ"
        4 -> "ТБ"
        else -> ""
    }

    val toUnitName = when (toUnit) {
        1 -> "КБ"
        2 -> "МБ"
        3 -> "ГБ"
        4 -> "ТБ"
        else -> ""
    }

    println("Результат: $value $fromUnitName = ${"%.6f".format(result)} $toUnitName")
}
