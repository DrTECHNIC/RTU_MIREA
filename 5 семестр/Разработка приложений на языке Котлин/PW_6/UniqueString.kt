class UniqueString {
    private var charArray: CharArray

    constructor(chars: CharArray)
    { charArray = chars }

    constructor(str: String)
    { charArray = str.toCharArray() }

    fun getChar(index: Int): Char {
        require(index in charArray.indices) { "Индекс $index выходит за границы строки" }
        return charArray[index]
    }

    fun length(): Int = charArray.size

    fun printString()
    { println(String(charArray)) }

    fun contains(substring: CharArray): Boolean
    { return String(charArray).contains(String(substring)) }

    fun contains(substring: String): Boolean
    { return String(charArray).contains(substring) }

    fun trimLeadingSpaces()
    { charArray = String(charArray).trimStart().toCharArray() }

    fun reverse()
    { charArray.reverse() }
}