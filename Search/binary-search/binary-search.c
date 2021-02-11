#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>

int64_t binary_search(int* haystack, int64_t size, int needle) {
    int64_t left = 0;
    int64_t right = size - 1;
    while (left <= right) {
        int64_t mid = (left + right) / 2;
        
        if (haystack[mid] == needle) {
            return mid;
        } else if (haystack[mid] < needle) {
            left = mid + 1;
        } else { // needle < haystack[mid]
            right = mid - 1;
        }
    }

    return -1;
}

int less_int(const void * lhs, const void * rhs) {
    if ( *((int*)lhs) > *((int*)rhs) ) {
        return 1;
    } else if ( *((int*)lhs) <  *((int*)rhs) ) {
        return -1;
    }

    return 0;
}

int main() {
    int number_count;
    int target_count;

    scanf("%d %d", &number_count, &target_count);

    int* numbers = (int*)malloc(sizeof(int) * number_count);
    for (int i = 0; i < number_count; i++) {
        scanf("%d", &numbers[i]);
    }

    qsort(numbers, number_count, sizeof(int), less_int);

    int target = 0;
    for (int i = 0; i < target_count; i++) {
        scanf("%d", &target);
        printf("%lld ", binary_search(numbers, number_count, target));
    }

    free(numbers);

}
