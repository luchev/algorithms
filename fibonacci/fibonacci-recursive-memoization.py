def fibonacci(n):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Pro: keeps backlog of calculated terms and if the function is called repeatedly on
        the same number it will run in O(1)
    Con: O(n) space and O(2n) running time in the general case
    """
    if not hasattr(fibonacci, "memory"):
        fibonacci.memory =  {}

    if n == 0 or n == 1:
        return 1
    elif n in fibonacci.memory:
        return fibonacci.memory[n]
    else:
        next = fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci.memory[n] = next
        return next

for i in range(10):
    print(fibonacci(i))