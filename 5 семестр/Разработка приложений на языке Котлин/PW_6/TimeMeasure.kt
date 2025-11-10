class TimeMeasure(
    private var hours: Int,
    private var minutes: Int,
    private var seconds: Int
) {

    init { validateTime(hours, minutes, seconds) }

    constructor(hours: Int, minutes: Int) : this(hours, minutes, 0)
    constructor(hours: Int) : this(hours, 0, 0)

    private fun validateTime(hours: Int, minutes: Int, seconds: Int) {
        require(hours in 0..23) { "Часы должны быть в диапазоне 0-23" }
        require(minutes in 0..59) { "Минуты должны быть в диапазоне 0-59" }
        require(seconds in 0..59) { "Секунды должны быть в диапазоне 0-59" }
    }

    fun display24HourFormat() {
        println("Время: ${formatTwoDigits(hours)}:" +
                "${formatTwoDigits(minutes)}:" +
                formatTwoDigits(seconds))
    }

    fun display12HourFormat() {
        val period = if (hours < 12) "am" else "pm"
        val displayHours = when (hours) {
            0, 12 -> 12
            else -> hours % 12
        }
        println("Время: ${formatTwoDigits(displayHours)}:" +
                "${formatTwoDigits(minutes)}:" +
                "${formatTwoDigits(seconds)} $period")
    }

    fun addTime(addHours: Int, addMinutes: Int, addSeconds: Int) {
        validateTime(addHours, addMinutes, addSeconds)
        val totalSeconds = seconds + addSeconds
        val totalMinutes = minutes + addMinutes + totalSeconds / 60
        val totalHours = hours + addHours + totalMinutes / 60
        seconds = totalSeconds % 60
        minutes = totalMinutes % 60
        hours = totalHours % 24
    }

    private fun formatTwoDigits(number: Int) = String.format("%02d", number)
}