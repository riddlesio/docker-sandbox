using System;
using System.Collections;
using System.IO;

class Program {
    static void Main() {

        do {
            string line = Console.ReadLine();
            string[] words = line.Split(' ');

            if (words.Length == 0) {
                continue;
            }

            if (words[0] == "action") {
                Random rnd = new Random();
                int choice = rnd.Next(1, 4);
                
                if (choice == 1) {
                    Console.WriteLine("rock");
                }
                else if (choice == 2) {
                    Console.WriteLine("paper");
                }
                else if (choice == 3) {
                    Console.WriteLine("scissors");
                }
            }

        } while (line !== null);
    }
}