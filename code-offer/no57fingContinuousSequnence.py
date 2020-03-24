def findcontinuousSequence(sum):
    if sum < 3:
        return []
    small = 1
    big = 2
    middle = (sum+1)//2
    result = []
    curSum = small + big
    while small < middle:
        if curSum == sum:
            result.append(list(range(small,big+1)))
        #  这样如果curSum -= small之后curSum刚好等于sum会进入死循环
        # elif curSum > sum:
        #     curSum -= small
        #     small += 1
        # else:
        #     big += 1
        #     curSum += big
        while curSum > sum and small < middle:
            curSum -= small
            small += 1
            if curSum == sum:
                result.append(list(range(small,big+1)))
        big += 1
        curSum += big
    return result

print(findcontinuousSequence(9))

