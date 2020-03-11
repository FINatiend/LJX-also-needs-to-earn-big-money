def MoreThanHalfNum(numbers,length):
    # 判断输入符合要求
    if not numbers and length<=0:
        return 0

    # 利用快排算法
    result = numbers[0]
    times = 1
    for i in range(1,length):
        if times == 0:
            result = numbers[i]
            times = 1
        elif numbers[i] == result:
            times += 1
        else:
            times -= 1

    sum = 0
    for item in numbers:
        if item == result:
            sum += 1
    return result if sum*2 > length else 0
