use std::io;
use std::str;
use std::io::Write;

extern crate rand;

use rand::Rng;

fn main() {
    loop {
        let mut input = String::new();
        match io::stdin().read_line(&mut input) {
            Ok(n) => {
                let words: Vec<&str> = input.split_whitespace().collect();

                if words.len() == 0 {
                  break;
                }

                if words[0] == "action" {
                    let mut rng = rand::thread_rng();
                    let choice: u32 = rng.gen_range(0, 3);

                    match choice {
                        0 => println!("rock"),
                        1 => println!("paper"),
                        _ => println!("scissors")
                    }
                }
            },
            _ => (),
        }
    }
}
