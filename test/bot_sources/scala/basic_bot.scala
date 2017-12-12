object Bot {
    def main(args: Array[String]): Unit = {
        while (true) {
            val line = readLine()
            if (line == null) {
                return
            }
            val words = line.split(" ")
            
            if (words(0) == "action") {
                val r = scala.util.Random
                val choice = r.nextInt(3)

                if (choice == 0) {
                    println("rock")
                } else if (choice == 1) {
                    println("paper")
                } else if (choice == 2) {
                    println("scissors")
                }
            }
        }
    }
}
