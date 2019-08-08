from matrix import *

def multiply(matrix1, matrix2):
    """
    Multiply 2 matrices naively
    
    Complexity (n = matrix rows/cols)
    Time complexity: O(n^3)
    """
    if not matrix1.canMultiply(matrix2):
        return matrix(0, 0)
    out = matrix(matrix1.rows, matrix2.cols)

    for i in range(matrix1.rows):
        for j in range(matrix2.cols):
            sum = 0
            for k in range(matrix1.cols):
                sum += matrix1.get(i, k) * matrix2.get(k, j)
            out.set(i, j, sum)
    
    return out

def test():
    m1 = matrix(2, 2)
    m1.data = [[1, 2], [3, 4]]

    m2 = matrix(2, 2)
    m2.data = [[2, 0], [3, 1]]

    result1 = multiply(m1, m2)
    if result1.data == [[8, 2], [18, 4]]:
        print("Success")
    else:
        print("Fail")

    m3 = matrix(2, 3)
    m4 = matrix(3, 2)
    m3.data = [[1, 2, 3], [4, 5, 6]]
    m4.data = [[1,1], [0, 0], [1, 1]]
    result2 = multiply(m3, m4)
    if result2.data == [[4, 4], [10, 10]]:
        print("Success")
    else:
        print("Fail")

test()
