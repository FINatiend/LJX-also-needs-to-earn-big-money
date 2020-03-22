def getMissingNum(numbers,length):
    if not numbers or length <= 0:
        return -1
    left = 0
    right = length - 1

    while(left<=right):
        middle = (left+right)//2
        if numbers[middle] != middle:
            if middle == 0 or numbers[middle-1] == middle-1:
                return middle
            right = middle - 1
        else:
            left = middle + 1

    #  缺了最后一个数字的情况
    if left == right+1:
        return left

    # 记得都不满足条件的情况
    return -1

data =[ 0 ]
print(getMissingNum(data,1))