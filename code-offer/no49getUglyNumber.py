def getUglyNumber(index):
    if index <= 0:
        return 0

    uglyNumberList = [0 for i in range(index)]
    uglyNumberList[0] = 1
    nextUgluIndex = 1
    index2 = index3 = index5 = 0

    # 直接用uglyNumberList就好了
    # multiply2List = multiply3List = multiply5List = uglyNumberList

    while(nextUgluIndex < index):
        min = getMin(uglyNumberList[index2]*2,uglyNumberList[index3]*3,uglyNumberList[index5]*5)

        uglyNumberList[nextUgluIndex] = min

        while uglyNumberList[index2] * 2 <= uglyNumberList[nextUgluIndex]:
            index2 += 1
        while uglyNumberList[index3] * 3 <= uglyNumberList[nextUgluIndex]:
            index3 += 1
        while uglyNumberList[index5] * 5 <= uglyNumberList[nextUgluIndex]:
            index5 += 1
        nextUgluIndex += 1
    ugly = uglyNumberList[nextUgluIndex-1]
    return ugly


def getMin(num1,num2,num3):
    min = min(min(num1,num2),num3)
    return min

