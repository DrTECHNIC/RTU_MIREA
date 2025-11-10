import java.io.File

class ErrorLogger<T> {
    private val logFile = File("errors.log")

    fun logError(error: T) {
        val message = when (error) {
            is String -> "String error: $error"
            is Number -> "Numeric error: $error"
            else -> "Unknown error type"
        }
        println(message)
        logFile.appendText("$message\n")
    }
}

fun <T> ErrorLogger<T>.logAndSend(error: T) {
    logError(error)
    println("Sending error to server...")
}

fun main() {
    val stringLogger = ErrorLogger<String>()
    stringLogger.logError("Network timeout")
    stringLogger.logAndSend("Database connection failed")

    val numberLogger = ErrorLogger<Number>()
    numberLogger.logError(404)
    numberLogger.logAndSend(500)
}
