def lastRemaining(n,m):
    if n < 1 or m < 1:
        return -1

    numberList = [i for i in range(n)]

    current = 0
    while len(numberList) > 1:
        current = (current + m-1) % len(numberList)
        numberList.remove(numberList[current])

    return numberList[0]

# 时间和空间都减小了三分之一，，找规律递推
def lastRemainingv2(n,m):
    if n < 1 or m < 1:
        return -1
    x = 0
    for i in range(2,n+1):
        x = (x+m)%i
    return x
print(lastRemainingv2(5,2))