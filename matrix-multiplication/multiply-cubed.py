from squareMatrix import *

def multiply(matrix1, matrix2):
    if matrix1.getSize() != matrix2.getSize():
        return []
    
    out = squareMatrix(matrix1.getSize())

    for i in range(matrix1.getSize()):
        for j in range(matrix1.getSize()):
            sum = 0
            for k in range(matrix1.getSize()):
                sum += matrix1.get(i, k) * matrix2.get(k, j)
            out.set(i, j, sum)
    
    return out


def test():
    m1 = squareMatrix(2)
    m1.data = [[1, 2], [3, 4]]

    m2 = squareMatrix(2)
    m2.data = [[2, 0], [3, 1]]

    result = multiply(m1, m2)
    if result.data == [[8, 2], [18, 4]]:
        print("Success")
    else:
        print("Fail")

test()
