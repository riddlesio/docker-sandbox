import java.util.Scanner;
import java.util.Random;


public class BasicBot {

 	public static void main(String[] args) {
 		Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        
        while (scan.hasNextLine()) {
            String line = scan.nextLine().trim();
            System.err.println(line);
            if(line.length() == 0) {
				continue;
			}

            String[] words = line.split(" ");
            if (!words[0].equals("action")) {
                continue;
            }

            int choice = rand.nextInt(3);
            if (choice == 0) {
                System.out.println("rock");
            }
            else if (choice == 1) {
                System.out.println("paper");
            }
            else {
                System.out.println("scissors");
            }
        }
 	}
 }
