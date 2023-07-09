use std::fs;
use std::{thread, time};
use std::collections::HashMap;

fn remove_chars(a: char, vec: Vec<char>) -> Vec<char> {
    let mut new_vec: Vec<char> = Vec::<char>::with_capacity(100000);

    for character in vec {
        if !character.eq_ignore_ascii_case(&a) {
            new_vec.push(character);
        }
    }
    return new_vec;
}

fn main() {
    let filepath = "input5.txt";

    let contents = fs::read_to_string(filepath).expect("Should be able to read file");

    let alphabet = "abcdefghijklmnopqrstuvwxyz".to_string();

    let mut map: HashMap<char, i32> = HashMap::new();

    for alpha_char in alphabet.chars() {
        let mut stack = Vec::<char>::with_capacity(100000);

        let letters = remove_chars(alpha_char, contents.chars().collect());

        for current in letters {
            
            // println!("{:?}", stack);
            if alpha_char == current {
                continue;
            }

            if stack.len() > 0 {
                let previous = stack.pop();

                if previous.unwrap() == current {
                    stack.push(previous.unwrap());
                    stack.push(current);
                } else if previous.is_some() { 
                    let previous_unwrapped = previous.unwrap();
                    if previous_unwrapped.eq_ignore_ascii_case(&current) {
                        continue;
                    } else {
                        stack.push(previous.unwrap());
                        stack.push(current);
                    }
                } else {
                    stack.push(previous.unwrap());
                    stack.push(current);
                } 
            } else {
                stack.push(current);
            }
        }
    map.insert(alpha_char, stack.len().try_into().unwrap());
    }
    println!("{:?}", map);
}
