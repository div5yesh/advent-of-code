import java.io.File
import java.util.*
import kotlin.Comparator

fun main() {
    println("AoC++ 2021")

    val gridInput = File("./grid.txt").useLines { lines ->
        lines.toList()
            .map {
                it.split("")
                    .map { i -> i.toIntOrNull() }.filterNotNull()
            }
    }
    println(riskPath(gridInput))
}

fun riskPath(grid: List<List<Int>>): Int {
    data class Node(var i:Int, var j:Int)
    val node = arrayOf(0, 0, 0)
    val compareByCost: Comparator<Array<Int>> = compareBy { it[0] }
    val queue = PriorityQueue(compareByCost)
    var visited = mutableSetOf<Node>()
    queue.add(node)
    while (!queue.isEmpty()) {
        val node = queue.peek()
        val (cost, i, j) = node
        visited.add(Node(i, j))
        queue.remove(node)
        val stepDeltas = arrayOf(arrayOf(0, 1), arrayOf(1, 0), arrayOf(-1, 0), arrayOf(0, -1))
        for (delta in stepDeltas) {
            val newI = i + delta[0]
            val newJ = j + delta[1]
            if (newI == grid.size - 1 && newJ == grid.size - 1)
                return cost + grid[newI][newJ]
            if (!visited.contains(Node(newI, newJ)) && newI >= 0 && newJ >= 0 && newI < grid.size && newJ < grid.size) {
                queue.add(arrayOf(cost + grid[newI][newJ], newI, newJ))
            }
        }
    }
    return 0
}