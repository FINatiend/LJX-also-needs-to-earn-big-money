def numberOf1(n):
    if n <= 0:
        return 0
    str1 = str(n)
    return numberOf1_Core(str1)

def numberOf1_Core(str1):
    if not str1 or str1[0] < '0' or str1[0] > '9':
        return 0

    length = len(str1)

    first = int(str1[0])

    if length == 1 and first == 0:
        return 0

    if length == 1 and first > 0:
        return 1

    # 若num是21345
    numFirstDIgit = 0
    # 先算第一位位1 的出现多少次，即10000——19999
    if first > 1:
        numFirstDIgit = powerBase10(length-1)
    #  这里不能直接用else，用else的话前面加一个判断first为0的
    elif first == 1:
        numFirstDIgit = int(str1[1:])+1

    # 1345～21345中除第一位外位1的数目，即这两万个数中1的个数
    numOfOtherDigits = first * (length-1) * powerBase10(length-2)

    numRecurise = numberOf1_Core(str1[1:])

    return numFirstDIgit + numOfOtherDigits + numRecurise

def powerBase10(n):
    result = 1
    for i in range(0,n):
        result *= 10

    return result

print(numberOf1(10000))