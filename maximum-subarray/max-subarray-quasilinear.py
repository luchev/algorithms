import math

def maxsubarray(list):
    return maxsubarrayRecursive(list, 0, len(list) - 1)

def maxsubarrayRecursive(list, start, end):
    if start - end == 0:
        return (list[start], start, end)
    
    left = maxsubarrayRecursive(list, start, math.floor((end + start)/2))
    right = maxsubarrayRecursive(list, math.ceil((end + start)/2), end)
    mid = maxsubarrayMid(list, start, math.floor((end + start)/2), end)

    if mid[0] > left[0] and mid[0] > right[0]:
        return mid
    elif left[0] > mid[0] and left[0] > right[0]:
        return left
    else:
        return right

def maxsubarrayMid(list, start, mid, end):
    leftMaxSum = -math.inf
    leftSum = 0
    leftIndex = mid
    for i in range(mid, start - 1, -1):
        leftSum += list[i]
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum
            leftIndex = i

    rightMaxSum = -math.inf
    rightSum = 0
    rightIndex = mid
    for i in range(mid + 1, end + 1):
        rightSum += list[i]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum
            rightIndex = i
    
    maxSum = 0
    if leftMaxSum != -math.inf:
        maxSum += leftMaxSum
    if rightMaxSum != -math.inf:
        maxSum += rightMaxSum
    return (maxSum, leftIndex, rightIndex)

def test():
    result = maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    if result[0] == 6:
        print("Success")
    else:
        print("Fail")

test()

