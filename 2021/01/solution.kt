import java.io.File
import java.util.*

fun main() {
    println("AoC++ 2021")

    val input = File("./sonar.txt").useLines { lines -> lines.toList().map { it.toInt() } }
    println(sumSonarSweep(input))
}

fun sonarWeep(arr: List<Int>): Int {
    var inc = 0
    for (i in 0 until arr.size - 1) {
        if (arr[i] < arr[i + 1]) inc++
    }
    return inc
}

fun sumSonarSweep(arr: List<Int>): Int {
    var inc = 0
    var sums = mutableListOf<Int>()
    for (i in 0 until arr.size - 2) {
        sums.add(arr[i] + arr[i + 1] + arr[i + 2])
    }
    for (i in 0 until sums.size - 1) {
        if (sums[i] < sums[i + 1]) inc++
    }
    return inc
}