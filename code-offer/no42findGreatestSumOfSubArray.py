def findSubarray(nums):
    invalidInput = False

    if not nums or len(nums) <= 0:
        invalidInput = True
        return 0

    invalidInput = False
    curSum = 0
    greastestSum = float('-inf')

    for i in nums:
        if curSum < 0:
            curSum = i
        else:
            curSum += i

        if curSum > greastestSum:
            greastestSum = curSum
    return greastestSum