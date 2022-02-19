// 2011. Final Value of Variable After Performing Operations

#include <stdio.h>
#include <string.h>

int finalValueAfterOperations(char **operations, int operationsSize) {
    int out = 0;
    for (int i = 0; i < operationsSize; i++) {
        // since strcmp returns 0 if equal and non zero otherwise
        if (!strcmp(operations[i], "++X") || !strcmp(operations[i], "X++")) {
            out++;
        }
        if (!strcmp(operations[i], "--X") || !strcmp(operations[i], "X--")) {
            out--;
        }
    }
    return out;
}

int main(int argc, char **argv) {
    char *operations[] = {"X++", "++X", "++X", "X--"};
    int operations_sz = sizeof(operations) / sizeof(operations[0]);
    printf("%d\n", finalValueAfterOperations(operations, operations_sz));
}