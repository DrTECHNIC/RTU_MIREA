import kotlin.random.Random

class Cat {
    private fun rest() { println("Sleep") }
    private fun voice() { println("Meow") }
    private fun feed() { println("Eat") }

    fun randomAction() {
        when (Random.nextInt(0, 3)) {
            0 -> rest()
            1 -> voice()
            2 -> feed()
        }
    }
}

class Student {
    private var firstName: String = ""
    private var lastName: String = ""
    private var scores: IntArray = IntArray(10)

    fun getFirstName(): String = firstName

    fun setFirstName(value: String)
    { firstName = value.trim().replaceFirstChar { it.uppercase() } }

    fun getLastName(): String = lastName

    fun setLastName(value: String)
    { lastName = value.trim().replaceFirstChar { it.uppercase() } }

    fun getScores(): IntArray = scores.copyOf()

    fun setScores(newScores: IntArray)
    { scores = newScores.copyOf() }

    fun addScore(newScore: Int)
    { scores = scores.copyOfRange(1, scores.size) + newScore }

    fun getAverageScore(): Double
    { return scores.average() }
}

class StudentService {
    fun findBestStudent(students: Array<Student>): Student?
    { return students.maxByOrNull { it.getAverageScore() } }

    fun sortStudentsByLastName(students: Array<Student>): Array<Student>
    { return students.sortedBy { it.getLastName() }.toTypedArray() }
}

fun main() {
    val cat = Cat()
    println("Задание 1:")
    repeat(3) { cat.randomAction() }


    val student = Student().apply {
        setFirstName("  имя  ")
        setLastName(" фамилия  ")
        setScores(intArrayOf(5, 4, 3, 5, 4, 3, 5, 4, 3, 5))
    }
    println("\nЗадание 2:")
    println("Имя: ${student.getFirstName()}")
    println("Фамилия: ${student.getLastName()}")
    println("Оценки: ${student.getScores().joinToString()}")
    println("Средний балл: ${student.getAverageScore()}")
    student.addScore(4)
    println("После добавления оценки: ${student.getScores().joinToString()}")
    println("Новый средний балл: ${student.getAverageScore()}")


    val students = arrayOf(
        Student().apply {
            setFirstName("Имя1")
            setLastName("Фамилия1")
            setScores(intArrayOf(5, 5, 5, 5, 5, 5, 5, 5, 5, 5))
        },
        Student().apply {
            setFirstName("Имя2")
            setLastName("Фамилия2")
            setScores(intArrayOf(3, 4, 3, 4, 3, 4, 3, 4, 3, 4))
        },
        Student().apply {
            setFirstName("Имя3")
            setLastName("Фамилия3")
            setScores(intArrayOf(4, 5, 4, 5, 4, 5, 4, 5, 4, 5))
        }
    )
    val service = StudentService()
    println("\nЗадание 3:")
    println("Лучший студент: ${service.findBestStudent(students)?.getLastName()}")
    val sortedStudents = service.sortStudentsByLastName(students)
    println("Отсортированный список:")
    sortedStudents.forEach { println(it.getLastName()) }
}