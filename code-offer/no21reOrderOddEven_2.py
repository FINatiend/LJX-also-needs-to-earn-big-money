# 对上一个解法进行扩展，要求其可重用
# 可把函数解耦成两部分
# 判断数字属于哪个标准；拆分数组进行调整
def reOrder(str,length,func):
    if length <= 0:
        return
    i = 0
    j = length - 1
    while i < j:
        while i < j and (not func(str[i])):
            i += 1
        while i < j and (func(str[j])):
            j -= 1

        if i < j:
            temp = str[j]
            str[j] = str[i]
            str[i] = temp


# 判断是否为偶数
def isEven(num):
    return (num & 1) == 0

def reOrderOddEven(str,length):
    reOrder(str,length,isEven)



# 测试用例
def printArray(str,length):
    if length <= 0 :
        return
    for i in range(0,length):
        print(str[i],end='')
    print("\t")

def Test(name,str,length):
    if len(name) != 0:
        print(name+"bagin")
    printArray(str,length)
    reOrderOddEven(str,length)
    printArray(str,length)

if __name__ == '__main__':
    str1 = [1, 2, 3, 4, 5, 6, 7]
    str2 = [2, 4, 6, 1, 3, 5, 7]
    str3 = [1, 3, 5, 7, 2, 4, 6]
    str4 = [1]
    str5 = [2]
    str6 = []
    Test("test1",str1,7)
    Test("test2",str2,7)
    Test("test3",str3,7)
    Test("test4",str4,1)
    Test("test5",str5,1)
    Test("test6",str6,0)
