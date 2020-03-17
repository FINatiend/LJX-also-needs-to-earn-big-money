def getTranslationCount_Num(number):
    if number < 0:
        return 0
    nuberToString = str(number)
    return getTranslationCount(nuberToString)

def getTranslationCount(numStr):
    length = len(numStr)
    countList = [0] * length
    count = 0

    for i in range(length-1,-1,-1):
        count = 0
        if i < length-1:
            count = countList[i+1]
        else:
            count = 1

        if i < length - 1:
            digit1 = int(numStr[i])
            digit2 = int(numStr[i+1])
            converted = int(digit1*10 + digit2)
            if converted >= 10 and converted <= 25:
                if i <length - 2:
                    count += countList[i+2]
                else:
                    count += 1
        countList[i] = count

    count = countList[0]
    return count
print(getTranslationCount_Num(10))


