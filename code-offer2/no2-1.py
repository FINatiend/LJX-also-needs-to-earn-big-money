# 1 有1个或多个重复数字
# 2 没有重复数字
# 3 特殊输入：空指针，空数组
# 4 特殊输入：长度为n的数组包含0～n-1之外的数字
def duplicate(numbers):
    length = len(numbers)
    if not numbers or length <= 0:
        return False

    newNumber = [0 for i in range(length)]
    for i in numbers:
        if i < 0 or i > length-1:
            return False
        if newNumber[i] != 0:
            return i
        else:
            newNumber[i] = 1
    return False




