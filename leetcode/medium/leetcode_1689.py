# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

# A decimal number is called deci-binary if each of its digits is either 0 or 1 without
# any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, return the minimum
# number of positive deci-binary numbers needed so that they sum up to n.

# Example 1:

# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32
# Example 2:

# Input: n = "82734"
# Output: 8
# Example 3:

# Input: n = "27346209830709182346"
# Output: 9

# for eg. in "82734"
# Sum of these 8 Deci-Binary numbers
# {11111, 11111, 10111, 10101,
# 10100, 10100, 10100, 10000} = 82734
# so the min nums of deci-Binary numbers for sum be n
# will always be = max digit in the num


class Solution:
    def minPartitions(self, n: str) -> int:
        return max([i for i in range(10) if str(i) in n])


testcase = [("32", 3), ("34", 4), ("82734", 8), ("27346209830709182346", 9)]
for i, v in enumerate(testcase):
    _ = Solution().minPartitions(v[0])
    print(f"\033[0mmin no of deci-bin nums: \033[0;93m{_}\033[0m for \033[0;93m{v[0]} ")
