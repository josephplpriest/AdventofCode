use std::fs;
use std::collections::HashMap;

fn main() {

    let file_path = "data/input1.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut total = 0;

    let mut map: HashMap<i32, bool> = HashMap::new();

    let mut answer_found = false;

    while !answer_found {
    
        let nums = contents.split("\n");

        for num in nums {
            let my_int = match num.parse::<i32>() {
                Ok(n) => n,
                Err(_) => {
                    println!("Failed to parse integer");
                    0
                },
            };
            total += my_int;

            if map.get(&total).is_some() {
                answer_found = true;
                println!("{}", total);
                break;
            } else {
                map.insert(total, true);
            };
            
        }
    }
    println!("{}", total);
}
