// 2114. Maximum Number of Words Found in Sentences

struct Solution {}
impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut most_words: i32 = 0;
        for (_i, x) in sentences.iter().enumerate() {
            let mut _num_words: i32 = x.split(" ").collect::<Vec<&str>>().len() as i32;
            if _num_words > most_words {
                most_words = _num_words;
            }
        }
        return most_words;
    }
}

fn main() {
    println!(
        "{:?}",
        Solution::most_words_found(vec![
            "this is great thanks very much".to_string(),
            "alice and bob love leetcode".to_string(),
            "i think so too".to_string(),
        ])
    );
}
