fun main()
{
    task1()
    task2()
}

fun task1()
{
    println("Введите строку ДНК:")
    val dna: String = readln()
    var a: Int = 0
    var t: Int = 0
    var g: Int = 0
    var c: Int = 0
    for (char in dna)
        when (char)
        {
            'A' -> a++
            'T' -> t++
            'G' -> g++
            'C' -> c++
        }
    println("$a $t $g $c")
}

fun task2()
{
    println("Введите сумму для размена:")
    val scan = java.util.Scanner(System.`in`)
    var n = scan.nextInt()
    val c8 = n / 8
    n %= 8
    val c4 = n / 4
    n %= 4
    val c2 = n / 2
    n %= 2
    val c1 = n
    println("$c8 $c4 $c2 $c1")
}