data class User(val name: String, val age: Int, val friends: List<User> = emptyList())

object UserList {
    private val users = mutableListOf<User>()

    fun addUser(user: User) {users.add(user)}
    fun findOldestUser(): User? {return users.maxByOrNull { it.age }}

    fun printOldestUserInfo() {
        val oldestUser = findOldestUser()
        if (oldestUser != null)
            println("Самый старший пользователь: ${oldestUser.name}, возраст: ${oldestUser.age}")
        else
            println("Список пользователей пуст")
    }

    fun printAllUsers() {
        println("Все пользователи:")
        users.forEach { user ->
            println(" - ${user.name}, возраст: ${user.age}, друзей: ${user.friends.size}")
        }
    }

    fun getUsers(): List<User> = users.toList()
    fun getUsersCount(): Int = users.size
    fun getAverageAge(): Double = users.map { it.age }.average()
    fun getUsersWithFriendsCount(): Int = users.count { it.friends.isNotEmpty() }
}

fun main() {
    val user1 = User("Алексей", 25)
    val user2 = User("Мария", 30)
    val user3 = User("Иван", 35)
    val user4 = User("Ольга", 28)
    val user5 = User("Дмитрий", 40, listOf(user1, user2))
    val user6 = User("Екатерина", 32, listOf(user3, user4, user5))

    UserList.addUser(user1)
    UserList.addUser(user2)
    UserList.addUser(user3)
    UserList.addUser(user4)
    UserList.addUser(user5)
    UserList.addUser(user6)

    UserList.printAllUsers()
    UserList.printOldestUserInfo()

    println("\nДополнительная статистика:")
    println("Всего пользователей: ${UserList.getUsersCount()}")
    println("Средний возраст: ${"%.2f".format(UserList.getAverageAge())}")
    println("Пользователей с друзьями: ${UserList.getUsersWithFriendsCount()}")
}