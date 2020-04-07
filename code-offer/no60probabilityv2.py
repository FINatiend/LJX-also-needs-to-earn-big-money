def probability(maxValue,number):
    if number < 1:
        return []

    maxSum = maxValue * number
    minSum = number
    totalnum = pow(maxValue,number)
    probabilityList = [[0 for i in range(minSum,maxSum+1)] for i in range(2)]
    ratioList = [0 for i in range(len(probabilityList))]

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


