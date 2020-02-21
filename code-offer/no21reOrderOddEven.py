def reOrderOddEven_1(str):
    length = len(str)
    if length == 0:
        return
    i = 0
    j = length - 1

    while i < j:
        #前面的为奇数，遇到偶数停止
        while i < j and (str[i] & 0x1) != 0:
            i += 1
        while i < j and (str[j] & 0x1) == 0:
            j -= 1

        if i < j:
            temp = str[j]
            str[j] = str[i]
            str[i] = temp
    return str


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
    str = reOrderOddEven_1(str)
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
