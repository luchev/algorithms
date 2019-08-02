def fibonacci(term):
    """
    Time complexity: O(2^n)
    Space complexity: O(n)

    Pro: short code
    Con: very slow code because of the recursion tree
    """
    if term == 0 or term == 1:
        return 1
    else:
        return fibonacci(term - 1) + fibonacci(term - 2)

for number in range(10):
    print(fibonacci(number))