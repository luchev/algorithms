#include "stdio.h"
#include "stdint.h"
#include "stdlib.h"

int64_t linear_search(int* haystack, size_t length, int needle) {
    for (int64_t i = 0; i < length; i++) {
        if (haystack[i] == needle) {
            return i;
        }
    }

    return -1;
}

int main() {
    int number_count;
    int target_count;
    scanf("%d %d", &number_count, &target_count);
    
    int* numbers = (int*)malloc(sizeof(int) * number_count);
    for (int i = 0; i < number_count; i++) {
        scanf("%d", &numbers[i]);
    }

    int target;
    for (int i = 0; i < target_count; i++) {
        scanf("%d", &target);
        printf("%lld ", linear_search(numbers, number_count, target));
    }

    free(numbers);
}
