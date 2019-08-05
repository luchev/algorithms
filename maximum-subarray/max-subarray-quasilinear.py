import math

def maxsubarray(list):
    return maxsubarrayRecursive(list, 0, len(list) - 1)

def maxsubarrayRecursive(list, start, end):
    """
    Calculate the max subarray in the left half (recursion)
    Calculate the max subarray in the right half (recursion)
    Calculate the maxsubarray crossing the middle
    Pick the best of the 3

    Complexity (n = length of input)
    Time complexity: O(nlogn)
    Space complexity: O(logn)
    """
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
    """
    Find the max subarray that crosses the mid point given
    Do this by naively finding the max subarray on the left side
    ending at position mid, and finding the max subarray on the 
    right side starting at position mid

    Time complexity: O(length if input)
    """
    leftMaxSum = -math.inf
    leftSum = 0
    leftIndex = mid
    # Find the left max subarray ending at mid
    for i in range(mid, start - 1, -1):
        leftSum += list[i]
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum
            leftIndex = i

    rightMaxSum = -math.inf
    rightSum = 0
    rightIndex = mid
    # Find the right max subarray starting at mid
    for i in range(mid + 1, end + 1):
        rightSum += list[i]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum
            rightIndex = i
    
    # Security checks in case there was no left/right subarray
    # This is for the edge cases when we have odd number of elements
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

