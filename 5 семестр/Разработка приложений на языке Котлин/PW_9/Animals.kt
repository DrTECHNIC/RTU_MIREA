import kotlin.random.Random

interface Birthable {fun giveBirth()}

interface MammalBirth : Birthable {
    override fun giveBirth() {println("Рожает живого детеныша")}
}

interface FishBirth : Birthable {
    override fun giveBirth() {println("Мечет икру")}
}

interface BirdBirth : Birthable {
    override fun giveBirth() {println("Откладывает яйца")}
}

interface Movable {
    fun move()
}

interface Flying : Movable {
    override fun move() {println("Летает")}
}

interface Swimming : Movable {
    override fun move() {println("Плавает")}
}

abstract class Animal(
    var name: String,
    var hunger: Int = Random.nextInt(0, 50),
    var energy: Int = Random.nextInt(50, 100),
    var happiness: Int = Random.nextInt(50, 100)
) {
    abstract val birthMethod: Birthable
    abstract val movement: Movable

    fun eat() {
        hunger = (hunger - 30).coerceAtLeast(0)
        energy += 10
        println("$name ест. Голод уменьшен, энергия восстановлена")
    }

    fun sleep() {
        energy = (energy + 40).coerceAtMost(100)
        hunger += 20
        println("$name спит. Энергия восстановлена, голод увеличился")
    }

    fun play() {
        happiness = (happiness + 30).coerceAtMost(100)
        energy -= 20
        hunger += 10
        println("$name играет. Счастье увеличено, энергия уменьшена")
    }

    fun checkStatus() {
        println("""
            Состояние $name:
            Голод: $hunger%
            Энергия: $energy%
            Счастье: $happiness%
        """.trimIndent()
        )
    }

    fun updateStatus() {
        hunger = (hunger + Random.nextInt(5, 15)).coerceAtMost(100)
        energy = (energy - Random.nextInt(5, 15)).coerceAtLeast(0)
        happiness = (happiness - Random.nextInt(5, 15)).coerceAtLeast(0)
    }
}

class Bat : Animal("Летучая мышь"), MammalBirth, Flying {
    override val birthMethod: Birthable = this
    override val movement: Movable = object : Flying {
        override fun move() {println("Медленно летает")}
    }
}

class Dolphin : Animal("Дельфин"), MammalBirth, Swimming {
    override val birthMethod: Birthable = this
    override val movement: Movable = object : Swimming {
        override fun move() {println("Быстро плавает")}
    }
}

class GoldFish : Animal("Золотая рыбка"), FishBirth, Swimming {
    override val birthMethod: Birthable = this
    override val movement: Movable = object : Swimming {
        override fun move() {println("Медленно плавает")}
    }
}

class Eagle : Animal("Орел"), BirdBirth, Flying {
    override val birthMethod: Birthable = this
    override val movement: Movable = object : Flying {
        override fun move() {println("Быстро летает")}
    }
}

fun animalMenu() {
    val animals = listOf(
        Bat(),
        Dolphin(),
        GoldFish(),
        Eagle()
    )

    while (true) {
        println("\n=== Меню управления животными ===")
        println("1. Показать всех животных")
        println("2. Взаимодействовать с животным")
        println("3. Выход")
        print("Выберите опцию: ")

        when (readLine()) {
            "1" -> {
                println("\nСписок животных:")
                animals.forEachIndexed { index, animal ->
                    println("${index + 1}. ${animal.name}")
                }
            }
            "2" -> {
                print("Введите номер животного: ")
                val input = readLine()?.toIntOrNull()
                if (input != null && input - 1 in animals.indices)
                    animalActions(animals[input - 1])
                else
                    println("Неверный номер!")
            }
            "3" -> return
            else -> println("Неверная опция!")
        }
    }
}

fun animalActions(animal: Animal) {
    while (true) {
        println("\n=== Взаимодействие с ${animal.name} ===")
        println("1. Покормить")
        println("2. Уложить спать")
        println("3. Играть")
        println("4. Показать способ рождения")
        println("5. Показать способ передвижения")
        println("6. Показать статус")
        println("7. Обновить статус")
        println("8. Назад")
        print("Выберите действие: ")

        when (readLine()) {
            "1" -> animal.eat()
            "2" -> animal.sleep()
            "3" -> animal.play()
            "4" -> animal.birthMethod.giveBirth()
            "5" -> animal.movement.move()
            "6" -> animal.checkStatus()
            "7" -> {
                animal.updateStatus()
                println("Статус обновлен!")
            }
            "8" -> return
            else -> println("Неверное действие!")
        }
    }
}

fun main() {animalMenu()}
