from matrix import *

def split(t):
    """
    Split a matrix into 4 squares
    doesn't work well for matrices of size < 2x2
    """
    midRow = int(t.rows/2)
    midCol = int(t.cols/2)
    topLeft = t.subMatrix(0, 0, midRow - 1, midCol - 1)
    topRight = t.subMatrix(0, midCol, midRow - 1, t.cols - 1)
    bottomLeft = t.subMatrix(midRow, 0, t.rows - 1, midCol - 1)
    bottomRight = t.subMatrix(midRow, midCol, t.rows - 1, t.cols - 1)
    return (topLeft, topRight, bottomLeft, bottomRight)

def merge(TL, TR, BL, BR):
    """
    Merge 4 squares of a matrix into one [ [TL, TR], [BL, BR]]
    """
    out = matrix(TL.rows + BL.rows, TL.cols + TR.cols)
    for i in range(TL.rows):
        for j in range(TL.cols):
            out.set(i, j, TL.get(i, j))
    for i in range(TR.rows):
        for j in range(TR.cols):
            out.set(i, j + TL.cols, TR.get(i, j))
    for i in range(BL.rows):
        for j in range(BL.cols):
            out.set(i + TL.rows, j, BL.get(i, j))
    for i in range(BR.rows):
        for j in range(BR.cols):
            out.set(i + TL.rows, j + TL.cols, BR.get(i, j))
    return out

def multiplyRecursive(m1, m2):
    """
    Split the matrices in 4 squares and recurse in each of them
    """
    out = matrix(m1.rows, m1.cols)
    if m1.rows == 1:
        out.set(0, 0, m1.get(0, 0) * m2.get(0, 0))
        return out
    
    a = split(m1)
    b = split(m2)

    topLeft = multiplyRecursive(a[0], b[0]) + multiplyRecursive(a[1], b[2])
    topRight = multiplyRecursive(a[0], b[1]) + multiplyRecursive(a[1], b[3])
    bottomLeft = multiplyRecursive(a[2], b[0]) + multiplyRecursive(a[3], b[2])
    bottomRight = multiplyRecursive(a[2], b[1]) + multiplyRecursive(a[3], b[3])

    return merge(topLeft, topRight, bottomLeft, bottomRight)
    

def multiplySquare(matrix1, matrix2):
    """
    Multiply square matrices whose size is powers of two recursively
    Must be a power of 2 because of the splitting method
    which cannot handle matrices of size < 2x2 because of the splitting
    and returns empty matrices which breaks the algorothm
    """
    if not matrix1.canMultiply(matrix2):
        return matrix(0, 0)
    return multiplyRecursive(matrix1, matrix2)
    
def multiply(matrix1, matrix2):
    """
    Multiply 2 matrices by first filling them up with zeros to become of size
    2^n x 2^n matrices and then multiplying them recursively

    Complexity (n = matrix rows/cols)
    Time complexity: O(n^3)
    """
    m1 = matrix1
    m1.fillToSquare()
    m2 = matrix2
    m2.fillToSquare()
    output = multiplySquare(m1, m2)
    output.removeEmptyCells()
    return output


def test():
    m1 = matrix(2, 2)
    m1.data = [[1, 2], [3, 4]]
    m2 = matrix(2, 2)
    m2.data = [[2, 0], [3, 1]]
    expectedResult1 = [[8, 2], [18, 4]]
    result1 = multiply(m1, m2)

    if result1.data == expectedResult1:
        print("Success")
    else:
        print("Fail")

    m3 = matrix(4, 4)
    m3.data = [[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14], [16, 17, 18, 19]]
    result2 = multiply(m3, m3)
    expectedResult2 = [[110, 120, 130, 140], [280, 310, 340, 370], [450, 500, 550, 600], [620, 690, 760, 830]]
    
    if result2.data == expectedResult2:
        print("Success")
    else:
        print("Fail")

    m4 = matrix(5, 5)
    m4.data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    result3 = multiply(m4, m4)
    expectedResult3 = [[215, 230, 245, 260, 275], [490, 530, 570, 610, 650], [765, 830, 895, 960, 1025], [1040, 1130, 1220, 1310, 1400], [1315, 1430, 1545, 1660, 1775]]
    
    if result3.data == expectedResult3:
        print("Success")
    else:
        print("Fail")

test()
