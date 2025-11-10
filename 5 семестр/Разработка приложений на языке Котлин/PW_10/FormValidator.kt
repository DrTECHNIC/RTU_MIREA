import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.time.format.DateTimeParseException

enum class Gender {MALE, FEMALE}
class NameValidationException(message: String) : Exception(message)
class BirthdateValidationException(message: String) : Exception(message)
class GenderValidationException(message: String) : Exception(message)
class WeightValidationException(message: String) : Exception(message)

class FormValidator {

    fun validateName(name: String): Boolean {
        if (name.length !in 2..20)
            throw NameValidationException("Имя должно содержать от 2 до 20 символов")
        if (!name[0].isUpperCase())
            throw NameValidationException("Первая буква имени должна быть заглавной")
        return true
    }

    fun validateBirthdate(birthdate: String): Boolean {
        val formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy")
        try {
            val date = LocalDate.parse(birthdate, formatter)
            val minDate = LocalDate.of(1900, 1, 1)
            val currentDate = LocalDate.now()
            if (date.isBefore(minDate))
                throw BirthdateValidationException("Дата рождения не может быть раньше 01.01.1900")
            if (date.isAfter(currentDate))
                throw BirthdateValidationException("Дата рождения не может быть в будущем")
        } catch (e: DateTimeParseException) {
            throw BirthdateValidationException("Неверный формат даты. Используйте dd.MM.yyyy")
        }
        return true
    }

    fun validateGender(gender: String): Boolean {
        try {
            Gender.valueOf(gender.uppercase())
        } catch (e: IllegalArgumentException) {
            throw GenderValidationException("Пол должен быть 'Male' или 'Female'")
        }
        return true
    }

    fun validateWeight(weight: String): Boolean {
        try {
            val weightValue = weight.toDouble()
            if (weightValue <= 0)
                throw WeightValidationException("Вес должен быть положительным числом")
        } catch (e: NumberFormatException) {
            throw WeightValidationException("Вес должен быть числом")
        }
        return true
    }

    fun validateForm(name: String, birthdate: String, gender: String, weight: String): Boolean {
        return validateName(name) && validateBirthdate(birthdate) && validateGender(gender) && validateWeight(weight)
    }
}

fun main() {
    val validator = FormValidator()

    try {
        validator.validateForm(
            "Иван",
            "15.05.1990",
            "MALE",
            "75.5"
        )
        println("Анкета прошла проверку успешно!")
    } catch (e: Exception) {
        println("Ошибка: ${e.message}")
    }

    try {
        validator.validateForm(
            "иван", //маленькая буква
            "15.05.1990",
            "MALE",
            "75.5"
        )
    } catch (e: Exception) {
        println("Ошибка валидации: ${e.message}")
    }
}