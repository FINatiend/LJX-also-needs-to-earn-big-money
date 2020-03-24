def findNumsWIthSum(data,length,sum):
    if not data or length <= 0:
        return []
    start = 0
    end = length - 1

    while start < end :
        curSum = data[start] + data[end]
        if curSum == sum:
            num1 = data[start]
            num2 = data[end]
            return [num1,num2]
        elif curSum > sum:
            end -= 1
        else:
            start += 1

    return []

data = [1,2,4,7,11,15]
print(findNumsWIthSum(data,6,15))