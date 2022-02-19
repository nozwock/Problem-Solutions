# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])

if __name__ == "__main__":
    testCase = [[1,2,3],[3,2,1]]
    res = Solution().maximumWealth(testCase)
    assert res == 6
    print(res)