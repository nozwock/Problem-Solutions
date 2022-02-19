// 2114. Maximum Number of Words Found in Sentences

struct Solution {}
impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut most_words: i32 = 0;
        for (_i, x) in sentences.iter().enumerate() {
            most_words = x.split(" ").collect::<Vec<&str>>().len() as i32;
        }
        return most_words;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::most_words_found(vec![
            "alice and bob love leetcode".to_string(),
            "i think so too".to_string(),
            "this is great thanks very much".to_string(),
        ])
    );
}
