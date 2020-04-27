# 1 有1个或多个重复数字
# 2 没有重复数字
# 3 特殊输入：空指针，空数组
# 4 特殊输入：长度为n的数组包含0～n-1之外的数字
def duplicate(numbers):
    length = len(numbers)
    if not numbers or length <= 0:
        return False

    for i in range(length):
        if numbers[i] < 0 or numbers[i] > length - 1:
            return False
        while numbers[i] != i:
            if numbers[numbers[i]] == numbers[i]:
                return True
            temp = numbers[i]
            numbers[i] = numbers[temp]
            numbers[temp] = temp


    return False

print(duplicate([3,1,2,0,2,5,3]))





