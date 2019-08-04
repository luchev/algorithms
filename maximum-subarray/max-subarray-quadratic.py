def maxsubarray(list):
    maxStart = 0
    maxEnd = 0
    maxSum = list[0]

    for i in range (len(list)):
        currentSum = 0
        for j in range (i, len(list)):
            currentSum += list[j]
            if currentSum > maxSum:
                maxSum = currentSum
                maxStart = i
                maxEnd = j
    return (maxSum, maxStart, maxEnd)

def test():
    result = maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    if result[0] == 6:
        print("Success")
    else:
        print("Fail")


test()