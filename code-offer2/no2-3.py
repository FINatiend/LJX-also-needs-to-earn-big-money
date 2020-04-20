# 1 有1个或多个重复数字
# 2 没有重复数字
# 3 特殊输入：空指针，空数组
# 4 特殊输入：长度为n的数组包含0～n-1之外的数字
def duplicate(numbers):
    length = len(numbers)
    if not numbers or length <= 0:
        return False

    for i in numbers:
        if i < 1 or i > length-1:
            return False

    start = 1
    end = length-1
    while(end >= start):
        count = 0
        middle = (end-start)//2+start
        for num in numbers:
            if num >= start and num <= middle:
                count += 1
        if count > middle-start+1:
            end = middle
        else:
            start = middle + 1

        if start == end:
            if count > 1:
                return True

    return False

print(duplicate([2,4,3,1,4]))




