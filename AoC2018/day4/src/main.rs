use std::fs;
use chrono::NaiveDateTime;
use std::str::FromStr;
use std::collections::HashMap;
use regex::Regex;

#[derive(Debug, Eq, Ord, PartialEq, PartialOrd)]
struct LogEntry {
    timestamp: NaiveDateTime,
    action: String
}

impl FromStr for LogEntry {
    type Err = Box<dyn std::error::Error>;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let timestamp_end = s.find(']').ok_or("Could not find closing bracket")?;
        let timestamp_str = &s[1..timestamp_end];
        let timestamp = NaiveDateTime::parse_from_str(timestamp_str, "%Y-%m-%d %H:%M")?;

        let action = s[(timestamp_end+2)..].to_string();

        Ok(LogEntry {
            timestamp,
            action,
        })
    }
}

fn main() {

    let file_path: &str = "input4.txt";

    let contents: String = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let parts = contents.split('\n');

    let collection = parts.collect::<Vec<&str>>();

    let entries: Result<Vec<LogEntry>, _> = collection
    .iter()
    .map(|line| line.parse::<LogEntry>())
    .collect();
    
    let mut valid_entries = entries.unwrap();

    valid_entries.sort();

    let mut guards: HashMap<String, Vec<i32>> = HashMap::new();

    for entry in valid_entries {
        
        let current_guard: String;

        if entry.action.find('#').is_some() {
            // split on whitespace

            let re = Regex::new(r"#(\d+)").unwrap();

            let caps = re.captures(&entry.action).unwrap();

            let id = caps[1].to_string();

            current_guard = id;

            guards.entry(current_guard).or_insert(vec![0,60]);
        }

        


    }

}
