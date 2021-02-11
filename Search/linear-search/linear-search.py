import sys

def linear_search(haystack: list, needle: int) -> int:
    for index, val in enumerate(haystack):
        if val == needle:
            return index
    return -1

def test():
    input = sys.stdin.readlines()
    inputSplit = list(map(lambda x: x.split(), input))
    numbers = list(map(lambda x: int(x), inputSplit[1]))
    queries = list(map(lambda x: int(x), inputSplit[2]))
    for query in queries:
        print(linear_search(numbers, query), end=' ')

def main():
    if __name__ == '__main__':
        test()

main()
