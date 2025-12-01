object Task1 {
    fun run() {
        val listA = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        val listB = listOf(5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
        val setA = listA.toSet()
        val setB = listB.toSet()
        println("ListA (покупались): $listA")
        println("ListB (на складе): $listB")
        println()
        val boughtAndInStock = setA.intersect(setB)
        println("1. Товары, которые покупались и находятся на складе: $boughtAndInStock")
        val boughtButNotInStock = setA.subtract(setB)
        println("2. Товары, которые покупались, но отсутствуют на складе: $boughtButNotInStock")
        val allUniqueIds = setA.union(setB)
        println("3. Все уникальные ID товаров: $allUniqueIds")
        println()
    }
}
