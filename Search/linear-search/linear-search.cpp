#include <vector>
#include <iostream>
using namespace std;

int64_t linear_search(const vector<int>& haystack, int needle) {
    for (size_t i = 0; i < haystack.size(); i++) {
        if (haystack[i] == needle) {
            return i;
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

    for (int i = 0; i < target_count; i++) {
        int target;
        cin >> target;
        cout << linear_search(numbers, target) << " ";
    }
}

int main() {
    test();
}
