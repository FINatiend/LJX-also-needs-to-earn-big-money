#大数的输出，不能直接一轮循环
def PrintToMAxOfDIgits(n):
    if n <= 0:
        return
    number = [0] * (n+1)
    for i in range(0,10):
        number[0] = i
        PrintToMAxOfDIgitsRecurively(number,n,0)

def PrintToMAxOfDIgitsRecurively(number,length,index):
    if index == length - 1:
        PrintNumber(number)
        return

    for i in range(0,10):
        number[index+1] = i
        PrintToMAxOfDIgitsRecurively(number,length,index+1)

#递归输出

def printNNUm(n):
    if n <= 0:
        return
    number = [0]*n

    printNNumRecurively(number,n,0)

def printNNumRecurively(number,length,index):
    if index == length - 1:
        for i in range(0,10):
            number[index] = i
            PrintNumber(number)
        return

    for i in range(0,10):

        number[index] = i
        printNNumRecurively(number,length,index+1)



def PrintNumber(number):
    isBegining = True

    for i in range(0,len(number)):
        if isBegining and number[i] != 0:
            isBegining = False

        if not isBegining:
            print(number[i],end='')

    print("\n")


PrintToMAxOfDIgits(2)
# printNNUm(3)