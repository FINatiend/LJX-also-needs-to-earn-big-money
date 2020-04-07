def probability(maxValue,number):
    if number < 1:
        return []
    maxSum = number * maxValue
    minSum = number
    totalNum = pow(maxValue,number)

    probabilityList = [0 for i in range(minSum-number,maxSum-number+1)]

    Core(number,maxValue,0,probabilityList)

    ratioLiat = [0 for i in range(len(probabilityList))]

    for i in range(len(probabilityList)):
        ratioLiat[i] = probabilityList[i]/totalNum
        print(ratioLiat[i],end=' ')




def Core(n,maxValue,sum,probabilityList):
    if n == 0:
        probabilityList[sum-maxValue] += 1
    else:
        for i in range(1,maxValue+1):
            Core(n-1,maxValue,sum+i,probabilityList)

probability(6,2)