def isContinuous(list):
    length = len(list)
    if not list:
        return False

    list.sort()

    numberOfZero = 0
    numberOfGap = 0

    for i in list:
        if i == 0:
            numberOfZero += 1

    # 这里必须从numberOfZero开始，，因为当有0存在时，要从其开始的后一个位置算gap
    for i in range(numberOfZero,length-1):
        # 前后相等，绝对不是顺子
        if list[i] == list[i+1]:
            return False

        numberOfGap += (list[i+1]-list[i]-1)

    return numberOfZero >= numberOfGap

# print(isContinuous([1,3,2,5,4]))
print(isContinuous([0,3,2,6,4]))