// 1929. Concatenation of Array

// Given an integer array nums of length n, you want to create an array ans of
// length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
// (0-indexed).

// Specifically, ans is the concatenation of two nums arrays.

// Return the array ans.

#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *getConcatenation(int *nums, int numsSize, int *returnSize) {
  *returnSize = 2 * numsSize;
  int *out = malloc(*returnSize * sizeof(int));
  for (int i = 0; i < numsSize; i++) {
    out[i] = nums[i];
    out[i + numsSize] = nums[i];
  }
  return out;
}

int main(int argc, char **argv) {
  int nums[] = {1, 2, 1};
  int nums_n = sizeof(nums) / sizeof(int);
  int r_size;
  int *concat_arr = getConcatenation(nums, nums_n, &r_size);

  for (int i = 0; i < r_size; i++) {
    printf("%d, ", concat_arr[i]);
  }
  printf("\n");
  free(concat_arr);
}