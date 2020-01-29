def PrintToMAxDIgits(n):
    if n <= 0:
        return
    number = [0]*(n)

    while(not Increment(number)):
        PrintNumber(number)


def Increment(number:[int]):
    isOverflow = False
    nTakeOver = 0
    length = len(number)

    #每一轮只计一个数，这个循环存在的意义仅在于判断是否有进位，如有进位，高位就可以加nTakeove
    # 以isOverflow判断是否最高位进位，最高位进位则溢出，整个结束输出。
    for i in range(length-1,-1,-1):
        nSum = number[i] + nTakeOver
        if i == length -1:
            nSum += 1

        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = nSum
        else:
            number[i] = nSum
            break

    return isOverflow

def ifIncrement(number):
    isOverflow = False
    nTakeOver = 0

    length = len(number)-1

    for i in range(length,-1,-1):
        nSum = number[i] + nTakeOver
        if i == length:
            nSum += 1

        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                number[i] = nSum
                nTakeOver = 1
        else:
            number[i] = nSum
            break
    return isOverflow




def PrintNumber(number:[int]):
    isBegining = True

    for i in range(0,len(number)):
        if isBegining and number[i] != 0:
            isBegining = False

        if not isBegining:
            print(number[i],end='')

    print("\n")

PrintToMAxDIgits(2)