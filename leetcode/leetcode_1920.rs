struct Solution {}
impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut out: Vec<i32> = Vec::with_capacity(nums.len());
        for (_i, x) in nums.iter().enumerate() {
            out.push(nums[*x as usize]);
        }
        return out;
    }
}

fn main() {
    println!("{:?}", Solution::build_array(vec![0, 2, 1, 5, 3, 4]));
}
