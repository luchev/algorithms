def fibonacci(n):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Pro: fastest calculation of a single fibonacci term
    Con: has to recalculate everything from 0 each time the function is called
    """
    previous = 0
    current = 1
    for _ in range(n):
        previous, current = current, current + previous
    return current

for i in range(10):
    print(fibonacci(i))
