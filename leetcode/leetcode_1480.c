// 1480. Running Sum of 1d Array

#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *runningSum(int *nums, int numsSize, int *returnSize) {
    *returnSize = numsSize;
    int *out = malloc(*returnSize * sizeof(int));
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
        out[i] = sum;
    }
    return out;
}

int main(int argc, char **argv) {
    int nums[] = {1, 2, 3, 4};
    int nums_n = sizeof(nums) / sizeof(int);
    int r_size;
    int *sum_arr = runningSum(nums, nums_n, &r_size);

    for (int i = 0; i < r_size; i++) {
        printf("%d, ", sum_arr[i]);
    }
    printf("\n");
    free(sum_arr);
}