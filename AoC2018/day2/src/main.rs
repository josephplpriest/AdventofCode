use std::fs;
use itertools::izip;

fn main() {
    
    let file_path: &str = "src/input2.txt";

    let contents: String = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    // let mut counter3s: i32 = 0;
    
    // let mut counter2s: i32 = 0;
    let parts = contents.split('\n');

    let keys = parts.collect::<Vec<&str>>();

    let stop = keys.len();

    for i in 0..stop {
        for j in (i+1)..stop {
            let first_key = keys[i].as_bytes();
            let second_key = keys[j].as_bytes();

            let mut counter: i32 = 0;

            for (a, b) in izip!(first_key, second_key) {
                    if a == b {
                    counter += 1
                    }
                }
            

            if counter == 25 {
                println!("{}", keys[i]);
                println!("{}", keys[j]);
            }
        }
    }
}

    //     let word_vec: Vec<char> = line.chars().collect(); 
        
    //     let mut map: HashMap<char, i32> = HashMap::new();

    //     for letter in word_vec {
    //         let count: &mut i32 = map.entry(letter).or_insert(0);
    //         *count += 1;
    //     }

    //     let mut has_two: bool = false;
    //     let mut has_three: bool = false;

    //     for c in map.values() {
    //         if *c == 3 {
    //             has_three = true;
    //         }
    //         if *c == 2 {
    //             has_two = true;
    //         }
    //     }
    //     if has_two {
    //         counter2s += 1;
    //     }
    //     if has_three {
    //         counter3s += 1;
    //     }

    // }

    // println!("{}", counter2s * counter3s);
