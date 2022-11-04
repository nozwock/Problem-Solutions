// 1470. Shuffle the Array

struct Solution {}
impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut out: Vec<i32> = Vec::with_capacity(2 * n as usize);
        for i in 0..n {
            out.push(nums[i as usize]);
            out.push(nums[(i + n) as usize]);
        }
        return out;
    }
}

fn main() {
    println!("{:?}", Solution::shuffle(vec![2, 5, 1, 3, 4, 7], 3))
}
