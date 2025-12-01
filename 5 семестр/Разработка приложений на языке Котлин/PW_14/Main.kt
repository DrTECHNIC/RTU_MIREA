import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)
    while (true) {
        print(
            """
            1. Задание 1
            2. Задание 2
            0. Выход
            Выберите действие: 
            """.trimIndent()
        )
        when (scanner.nextLine().toIntOrNull()) {
            1 -> Task1.run()
            2 -> Task2.run()
            0 -> break
        }
    }
}
