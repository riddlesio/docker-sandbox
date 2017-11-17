fun main(args : Array<String>) {
    val actions = listOf("rock", "paper", "scissors")

    while (true) {
        val line = readLine()
        if (line == null) {
            break
        }

        val stripped = line.trim()
        if (stripped.length == 0) {
            continue
        }

        val words = line.split(" ");
        if (words.size == 0) {
            continue
        }

        when (words.get(0)) {
            "action" -> {
                val choice = (Math.random() * 3).toInt()
                println(actions.get(choice))
            }
        }
    }
}
