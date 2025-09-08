fun main()
{
    task1()
    task2()
    task3()
}

fun task1()
{
    val N = readln().toInt()
    val ai = DoubleArray(N) {readln().toDouble()}
    println(ai.average())
}

fun task2() {
    val N = readln().toInt()
    val ai = IntArray(N) {readln().toInt()}
    var current = ai[0]
    var count = 1
    for (i in 1 until N)
    {
        if (ai[i] == current)
            count++
        else
        {
            println("$count $current")
            current = ai[i]
            count = 1
        }
    }
    println("$count $current")
}

fun task3()
{
    val N = readln().toInt()
    val set = mutableSetOf<String>()
    var p: String = ""
    repeat(N)
    {
        val s = readln()
        if (!set.add(s)) {p = s}
    }
    println(p)
}