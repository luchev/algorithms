import sys
import math

def binary_search(sorted_haystack: [], needle):
    left = 0
    right = len(sorted_haystack) - 1

    while left <= right:
        mid = math.ceil((left + right) / 2)
        if sorted_haystack[mid] == needle:
            return mid
        elif sorted_haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def test():
    query_size = sys.stdin.readline()
    numbers = sys.stdin.readline().strip().split()
    numbers = list(map(int, numbers))
    numbers.sort()
    targets = sys.stdin.readline().strip().split()
    targets = list(map(int, targets))
    
    for target in targets:
        print(binary_search(numbers, target), end=' ')

if __name__ == '__main__':
    test()

