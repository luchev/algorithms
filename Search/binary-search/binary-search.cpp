#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int64_t binary_search(vector<int> sorted_haystack, int needle) {
    int64_t left = 0;
    int64_t right = sorted_haystack.size() - 1;
    
    while (left <= right) {
        size_t mid = (left + right) / 2;
        if (sorted_haystack[mid] == needle) {
            return mid;
        } else if (sorted_haystack[mid] < needle) {
            left = mid + 1;
        } else { // needle < sorted_haystack[mid]
            right = mid - 1;
        }
    }

    return -1;
}

void test() {
    int number_count;
    int target_count;
    cin >> number_count;
    cin >> target_count;

    vector<int> numbers;
    for (int i = 0; i < number_count; i++) {
        int input;
        cin >> input;
        numbers.push_back(input);
    }

    // The input must be sorted
    sort(numbers.begin(), numbers.end());

    for (int i = 0; i < target_count; i++) {
        int target;
        cin >> target;
        cout << binary_search(numbers, target) << " ";
    }
}

int main() {
    test();
}
