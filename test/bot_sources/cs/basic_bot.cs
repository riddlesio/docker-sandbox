using System;
using System.Collections;
using System.IO;

class Bot {
    static void Main() {
        string line;

        while(true) {
            line = Console.ReadLine();
            if (line == null) {
                break;
            }

            string[] words = line.Split(' ');
            if (words.Length == 0) {
                continue;
            }

            if (words[0] != "action") {
                continue;
            }
            
            Random rnd = new Random();
            int choice = rnd.Next(1, 4);
            
            if (choice == 1) {
                Console.Write("rock\n");
            }
            else if (choice == 2) {
                Console.Write("paper\n");
            }
            else if (choice == 3) {
                Console.Write("scissors\n");
            }
        }
    }
}
