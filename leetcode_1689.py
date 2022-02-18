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

from pprint import PrettyPrinter

pp = PrettyPrinter(compact=True)

def minSumOfDeciBin(num: str) -> int:
    for i in range(10):
        if str(i) in num:
            out = i
    return out

def sumOfDeciBin(num: str) -> int:
    deciBin = []
    num = int(num)
    i = 0
    while num > 0:
        length = len(str(num))
        partial = "1" * length
        for j in range(length):
            if int(partial) <= num:
                break
            partial = partial[: length - 1 - j] + "0" + partial[length - 1 - j + 1 :]
        deciBin.append(int(partial))
        num = num - deciBin[i]
        i += 1

    # pp.pprint(deciBin)
    print(
        f"\033[0;91mTotal Sum of above \033[0;93m{len(deciBin)}\033[0;91m "
        + f"deci-binary numbers is \033[0;93m{sum(deciBin)}\033[0m"
    )
    return len(deciBin)


testcase = [("32", 3), ("34", 4), ("82734", 8), ("27346209830709182346", 9)]
for i, v in enumerate(testcase):
    print(f"via min func: {minSumOfDeciBin(v[0])}")
    print(f"\033[0;96m{v}\033[0m")
    _ = sumOfDeciBin(v[0])
    print()
