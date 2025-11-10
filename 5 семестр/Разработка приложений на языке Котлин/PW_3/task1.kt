import kotlin.random.Random

fun guessNumberGame() {
    val secretNumber = Random.nextInt(0, 1001)
    println("Компьютер загадал число от 0 до 1000. Попробуйте угадать!")

    while (true) {
        print("Введите ваше число: ")
        val input = readLine()?.toIntOrNull()
        when {
            input == null -> {
                println("Ошибка ввода! Введите целое число.")
                continue
            }
            input < 0 -> {
                println("Игра завершена.")
                return
            }
            input == secretNumber -> {
                println("Победа!")
                return
            }
            input < secretNumber -> println("Это число меньше загаданного.")
            else -> println("Это число больше загаданного.")
        }
    }
}

fun main() {
    guessNumberGame()
}