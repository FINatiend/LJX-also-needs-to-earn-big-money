def maxDiff(numbers):
    length = len(numbers)
    if not numbers or length<2:
        return 0

    min = numbers[0]
    maxDiff = numbers[1] - numbers[0]

    # 一轮遍历，一边保存i之前的最小值，一边记录当前与最小值的差值，保存最大值
    for i in range(2,length):
        if numbers[i-1]<min:
            min = numbers[i-1]

        currentDiff = numbers[i] - min
        if currentDiff > maxDiff:
            maxDiff = currentDiff

    return maxDiff

print(maxDiff([9,11,8,5,7,12,16,14]))
print(maxDiff([1,2]))