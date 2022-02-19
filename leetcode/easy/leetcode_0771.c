// 771. Jewels and Stones

// You're given strings jewels representing the types of stones that are jewels,
// and stones representing the stones you have. Each character in stones is a
// type of stone you have. You want to know how many of the stones you have are
// also jewels.

// Letters are case sensitive, so "a" is considered a different type of stone
// from "A".

// Example 1:

// Input: jewels = "aA", stones = "aAAbbbb"
// Output: 3
// Example 2:

// Input: jewels = "z", stones = "ZZ"
// Output: 0

#include <stdio.h>
#include <string.h>

int numJewelsInStones(char *jewels, char *stones) {
    int out = 0;
    for (int i = 0; i < strlen(stones); i++) {
        for (int j = 0; j < strlen(jewels); j++) {
            if (jewels[j] == stones[i]) {
                out++;
            }
        }
    }
    return out;
}

int main() {
    char jewels_1[50] = "aA";
    char stones_1[50] = "aAAbbbb";
    char jewels_2[50] = "z";
    char stones_2[50] = "ZZ";

    printf("%d %d\n", numJewelsInStones(jewels_1, stones_1),
           numJewelsInStones(jewels_2, stones_2));
}