interface Device
class Computer : Device
class Phone : Device
class OtherDevice : Device
class BestRepairEver {
    fun canRepair(device: Device): Boolean {
        return when (device) {
            is Computer, is Phone -> true
            else -> false
        }
    }
}

fun main() {
    val repairShop = BestRepairEver()
    val devices = listOf(Computer(), Phone(), OtherDevice())
    devices.forEach { device ->
        val result = repairShop.canRepair(device)
        println("Мастерская ${if (result) "может" else "не может"} починить ${device::class.simpleName}")
    }
}
