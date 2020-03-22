def getNumSameAsIndex(numbers,length):
    if not numbers or length <= 0:
        return -1

    left = 0
    right = length - 1
    while left <= right:
        middle = (left + right)//2
        if middle == numbers[middle]:
            return middle
        elif numbers[middle] < middle:
            left = middle + 1
        else:
            right = middle - 1

    return -1

nums = [10]
print(getNumSameAsIndex(nums,1))

