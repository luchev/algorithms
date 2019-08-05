def maxsubarray(list):
    """
    Find a maximum subarray following this idea:
        Knowing a maximum subarray of list[0..j]
        find a maximum subarray of list[0..j+1] which is either
        (I) the maximum subarray of list[0..j]
        (II) or is a maximum subarray list[i..j+1] for some 0 <= i <= j
        We can determine (II) in constant time by keeping a max
        subarray ending at the current j.
        This is done in the first if of the loop, where the max
        subarray ending at j is max(previousSumUntilJ + array[j], array[j])
        
        This works because if array[j] + sum so far is less than array[j]
        then the sum of the subarray so far is negative (and less than array[j]
        in case it is also negative) so it has a bad impact on the 
        subarray until J sum and we can safely discard it and start anew
        from array[j]

    Complexity (n = length of list)
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if len(list) == 0:
        return (-1, -1, 0)
    
    # keep the max sum of subarray ending in position j
    maxSumJ = list[0]
    # keep the starting index of the maxSumJ
    maxSumJStart = 0
    # keep the sum of the maximum subarray found so far
    maxSum = list[0]
    # keep the starting index of the current max subarray found
    maxStart = 0
    # keep the ending index of the current max subarray found
    maxEnd = 0
    for j in range(1, len(list)):
        if maxSumJ + list[j] >= list[j]:
            maxSumJ = maxSumJ + list[j]
        else:
            maxSumJ = list[j]
            maxSumJStart = j
        
        if maxSum < maxSumJ:
            maxSum = maxSumJ
            maxStart = maxSumJStart
            maxEnd = j

    return (maxSum, maxStart, maxEnd)

def test():
    result = maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    if result[0] == 6:
        print("Success")
    else:
        print("Fail")

test()