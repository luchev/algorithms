import math
import decimal

def fibonacci(n):
    """
    Calculate Nth fibonacci term in O(1)
    
    decimal.getcontext().prec needs to be higher the higher term
    of fibonacci we need
    """
    decimal.getcontext().prec = 100
    sqrt5 = decimal.Decimal(5).sqrt()
    return int((((1 + sqrt5)/2) ** n - ((1-sqrt5)/2) ** n) / sqrt5)


print(fibonacci(7))
