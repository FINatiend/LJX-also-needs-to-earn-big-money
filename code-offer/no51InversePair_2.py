import copy
def InverPair(data):
    if not data or len(data) <= 0:
        return 0

    copyData = copy.copy(data)
    count  = Core(data,copyData,0,len(data)-1)
    return count

def Core(data,copydata,start,end):

    if start == end:
        copydata[start] = data[start]
        return 0

    length = (end - start)//2

    left = Core(data,copydata,start,start+length)
    right = Core(data,copydata,start+length+1,end)

    # i初始化为前半段最后一个数字的下标,j为后半段
    i = start + length
    j = end
    # 辅助数组的指针，指向最后一位
    indexcopy = end
    count = 0

    while(i >= start and j >=start+length+1):
        if data[i] > data[j]:
            copydata[indexcopy] = data[i]
            indexcopy -=1
            i -=1
            count += j-start-length
        else:
            copydata[indexcopy] = data[j]
            indexcopy -= 1
            j -= 1

    while i >= start:
        copydata[indexcopy] = data[i]
        indexcopy -= 1
        i -= 1

    while j >= start +length:
        copydata[indexcopy] = data[j]
        indexcopy -= 1
        j -= 1

    return count +left +right

def Test():
    data1 = [6, 5, 4, 3, 2, 1 ]
    print(InverPair(data1))
Test()




