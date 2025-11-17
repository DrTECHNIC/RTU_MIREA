class UserProfile(
    val name: String? = null,
    val age: Int? = null,
    val hobby: String? = null,
    val favoriteColor: String? = null,
    val favoriteMovie: String? = null,
    val favoriteBook: String? = null
) {
    fun printProfileInfo() {
        println("Имя: ${name ?: "Не указано"}")
        println("Возраст: ${age ?: "Не указан"}")
        println("Хобби: ${hobby ?: "Не указано"}")
        println("Любимый цвет: ${favoriteColor ?: "Не указан"}")
        println("Любимый фильм: ${favoriteMovie ?: "Не указан"}")
        println("Любимая книга: ${favoriteBook ?: "Не указана"}")
        println()
    }
}

fun main() {
    val user1 = UserProfile(
        name = "Даниил",
        age = 19,
        hobby = "Смотреть на рабочий стол",
        favoriteColor = "Пурпурный",
        favoriteMovie = "Зелёная миля",
        favoriteBook = "Ученик рейнджера"
    )

    val user2 = UserProfile(
        name = "Сюзанна",
        hobby = "Чтение Лавкрафта",
        favoriteBook = "Зов Ктулху"
    )

    val user3 = UserProfile()

    user1.printProfileInfo()
    user2.printProfileInfo()
    user3.printProfileInfo()
}
