def probability(maxValue,number):
    if number < 1:
        return []

    maxSum = maxValue * number
    minSum = number
    totalnum = pow(maxValue,number)
    # 这里因为是从第一个骰子开始，即1-6开始，所以list不能从一开始就设为maxSum+1-number这样子
    # probabilityList = [[0 for i in range(maxSum+1-number)] for i in range(2)]

    probabilityList = [[0 for i in range(maxSum+1)] for i in range(2)]
    ratioList = [0 for i in range(len(probabilityList[0]))]

    flag = 0

    for i in range(1,maxSum+1):
        probabilityList[flag][i] = 1

    for k in range(2,number+1):
        for j in range(k):
            probabilityList[1-flag][j] = 0

        for j in range(k,maxValue*k+1):
            probabilityList[1-flag][j] = 0
            p = 1
            # 前期p必须<= k ，后期p<=maxValue
            while p <= j and p <= maxValue:
                probabilityList[1-flag][j] += probabilityList[flag,j-p]
                p += 1

        flag = 1- flag

    for i in range(len(probabilityList[0])):
        ratioList[i] = probabilityList[flag][i]/totalnum
        print(ratioList[i],end=' ')

probability(6,2)


